web: bin/start-stunnel gunicorn config.wsgi:application
worker: bin/start-stunnel python manage.py metaci_rqworker high medium default
worker_short: bin/start-stunnel honcho start -f Procfile_worker_short
dev_worker: bin/start-stunnel honcho start -f Procfile_dev_worker
robot_worker: bin/start-stunnel python manage.py metaci_rqworker robot
release: python manage.py migrate --noinput
