# gunicorn_config.py
bind = "0.0.0.0:8000"
workers = 3  
module = "myproject.wsgi:application" 


errorlog = "/var/log/gunicorn_error.log"
accesslog = "/var/log/gunicorn_access.log"
loglevel = "info"