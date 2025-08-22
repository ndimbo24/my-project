# Run migrations and collect static files during deployment
release: python manage.py migrate --noinput && python manage.py collectstatic --noinput

# Start the web server
web: gunicorn loan.wsgi

