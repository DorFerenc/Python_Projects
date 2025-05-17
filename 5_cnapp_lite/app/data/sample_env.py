 # Simulated AWS environment setup (moto)
from moto import mock_s3
import boto3

def setup_mock_s3_environment():
    mock = mock_s3()
    mock.start()

    s3 = boto3.client('s3', region_name='us-west-1')

    # Bucket 1: Safe bucket
    s3.create_bucket(Bucket='private-bucket')

    # Bucket 2: Public bucket
    s3.create_bucket(Bucket='public-bucket')
    s3.put_bucket_acl(Bucket='public-bucket', ACL='public-read')

    return mock
