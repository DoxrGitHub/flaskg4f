# Use the official Python image as the base image
FROM python:3.9

# Set the working directory
WORKDIR /

# Add the current directory to the container as /app
ADD . /app

# Run the command inside your image filesystem
RUN pip install -r /app/requirements.txt

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 5000

# Run the specified command within the container.
CMD [ "python", "/app/main.py" ]
