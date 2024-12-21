# Use the official Python image from the Docker Hub
FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file and .env into the container
COPY requirements.txt .

RUN apk add --no-cache \
    postgresql-client \
    postgresql-dev \
    gcc \
    musl-dev 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "echo 'Waiting for the database...'; while ! pg_isready -h db -p 5432 -U sampleuser; do sleep 1; done; echo 'Database is ready, running migrations...'; python3 manage.py makemigrations && python3 manage.py migrate; python3 manage.py runserver 0.0.0.0:8000"]
