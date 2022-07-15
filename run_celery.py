from venv import create
from apps.factory import celery, create_celery
app = create_celery()
app.app_context().push()