from celery import Celery

celery = Celery('app',
                backend="redis://redis:6379/0",
                broker="redis://redis:6379/0",
                include=['app.celery_task'])
# broker='amqp://guest:guest@rabbitmq:5672//',
