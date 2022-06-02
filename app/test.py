import boto3
from botocore.config import Config

# AWS configs for retry
MAX_ATTEMPTS = 10
RETRY_MODE = "standard"
RETRIES = {
    'max_attempts': MAX_ATTEMPTS,
    'mode': RETRY_MODE
}
# Create an S3 client



def init_aws_s3_client(access_key, secret_key, region):
    return init_aws_client(access_key, secret_key, 's3', region)


def init_aws_client(access_key, secret_key, service, region=None):
    """
    initiates AWS client with the provided configs
    :return:
    """
    if region:
        return boto3.client(
            service, aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region,
            config=Config(retries=RETRIES))

    return boto3.client(
        service, aws_access_key_id=access_key, aws_secret_access_key=secret_key, config=Config(retries=RETRIES))

