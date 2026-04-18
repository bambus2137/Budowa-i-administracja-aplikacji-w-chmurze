#!/bin/sh

echo "Running migrations..."
until python manage.py migrate --noinput; do
    echo "Database unavailable, retrying in 2s..."
    sleep 2
done

echo "Creating superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
EOF

echo "Starting server..."
exec "$@"
