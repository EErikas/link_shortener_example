#!/bin/sh

# Function to perform migrations
perform_migrations() {
  until nc -z db 5432; do
    echo "$(date) - waiting for database..."
    sleep 1
  done
  echo "Collecting migrations..."
  python manage.py makemigrations
  echo "Migration done, applying migrations"
  python manage.py migrate
  echo "Adding default admin user"
  python manage.py createsuperuser --noinput
}

# Check the mode and start the appropriate command
if [ "$MODE" = "dev" ]; then
  echo "Starting development server at http://0.0.0.0:8000"
  perform_migrations
  python manage.py runserver "0.0.0.0:8000"
elif [ "$MODE" = "prod" ]; then
  echo "Starting production server with Gunicorn at http://0.0.0.0:8000"
  perform_migrations
  gunicorn -b "0.0.0.0:8000" link_shortener.wsgi:application
else
  echo "Invalid mode. Supported modes: dev, prod"
  exit 1
fi