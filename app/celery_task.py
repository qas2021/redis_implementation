from app.celery_app import celery
from celery.schedules import crontab
import boto3
celery.conf.beat_schedule = {
    'run_every_minute':
        {'task': 'add',
         'schedule': crontab(minute='*/1'),
         'args': str(4)
         },
}

celery.conf.timezone = 'UTC'


@celery.task(bind=True, name="add")
def add(x, y):
    s3 = boto3.client('s3',
                        aws_access_key_id='AKIASDUZUPSRCCIV2X2K',
                        aws_secret_access_key='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')
    # s3 = boto3.client('s3')

    # Call S3 to list current buckets
    response = s3.list_buckets()

    # Get a list of all bucket names from the response
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    # Print out the bucket list
    print("Bucket List: %s" % buckets)
