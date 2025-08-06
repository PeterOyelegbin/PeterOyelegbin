FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Copy the current directory contents into the working directory
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Run the Django app via WSGI
CMD ["gunicorn", "peteroyelegbin.wsgi:application", "--bind", "0.0.0.0:8000"]
