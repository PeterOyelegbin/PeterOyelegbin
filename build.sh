#!/bin/bash
# Exit on error
set -o errexit

# Install Python dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Try to install setuptools separately if needed
pip install setuptools

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Apply any outstanding database migrations
python manage.py migrate

echo "Build completed successfully!"
