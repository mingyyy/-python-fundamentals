web: gunicorn learning_log.wsgi
web: python learning_log/manage.py collectstatic --noinput ; gunicorn --bind 0.0.0.0:$PORT learninglog.wsgi:application