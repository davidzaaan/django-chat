web: daphne dj-chat.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=dj-chat.settings -v2
