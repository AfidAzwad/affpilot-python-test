# affpilot-python-test

Need to install dependencies from `requirements.txt` file with command : 

    `pip install -r requirements.txt`

**Start Celery Worker** : `celery -A config worker --loglevel=info`

**Start Beat Scheduler** : `celery -A config beat --loglevel=info`