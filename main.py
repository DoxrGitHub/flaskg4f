from flask import Flask, request, jsonify
import g4f
import json
import asyncio

app = Flask(__name__)


@app.route('/gpt3', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        return 'Content-Type must be application/json', 400

    # Get the data from the request as a JSON string
    data = request.get_data(as_text=True)

    # Parse the JSON string into a Python dictionary
    data = json.loads(data)

    # Check if the 'content' key exists in the data dictionary
    if 'content' not in data:
        return 'Missing content in request data', 400
    if 'system' not in data:
        return 'Missing system in request data', 400

    user_message = data.get('content')
    system_message = data.get('system')
    allowed_models = [
        'gpt-3.5-turbo',
        'gpt-4'
    ]

    # Create a new event loop
    loop = asyncio.new_event_loop()
    # Set it as the current event loop in the current OS thread
    asyncio.set_event_loop(loop)

    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        provider=g4f.Provider.DeepAi,
        messages=[
            { "role": 'system', "content": system_message },
            { "role": 'user', "content": user_message },
        ]
    )

    # Set the Content-Type header of the response to application/json
    return jsonify(response), 200, {"Content-Type": "application/json"}

@app.route('/gpt4', methods=['POST'])
def process_json2():
    # Check if the Content-Type header is set to 'application/json'
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        return 'Content-Type must be application/json', 400

    # Get the data from the request as a JSON string
    data = request.get_data(as_text=True)

    # Parse the JSON string into a Python dictionary
    data = json.loads(data)

    # Check if the 'content' key exists in the data dictionary
    if 'content' not in data:
        return 'Missing content in request data', 400
    if 'system' not in data:
        return 'Missing system in request data', 400

    user_message = data.get('content')
    system_message = data.get('system')

    # Create a new event loop
    loop = asyncio.new_event_loop()
    # Set it as the current event loop in the current OS thread
    asyncio.set_event_loop(loop)

    response = g4f.ChatCompletion.create(
        model="gpt-4",
        provider=g4f.Provider.Bing,
        messages=[
            { "role": 'system', "content": system_message },
            { "role": 'user', "content": user_message },
        ]
    )

    # Set the Content-Type header of the response to application/json
    return jsonify(response), 200, {"Content-Type": "application/json"}


if __name__ == '__main__':
    app.run(host="0.0.0.0")
