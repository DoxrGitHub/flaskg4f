# 1. Base image
FROM python:3.9

# 2. Copy files
COPY . /

# 3. Install dependencies
RUN pip install -r /requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]
