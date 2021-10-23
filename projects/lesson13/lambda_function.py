import boto3

from urllib.parse import unquote_plus


def lambda_handler(event, context):
    print(event)
    s3 = boto3.client('s3')
    store_bucket = 'armen-manukyan-store'
    upload_bucket = event['Records'][0]['s3']['bucket']['name']
    key = unquote_plus(event['Records'][0]['s3']['object']['key'])

    s3_obj = s3.get_object(Bucket=upload_bucket, Key=key)
    print(s3_obj)
    body = s3_obj['Body'].read().decode()
    body += '\nWelcome to the Lambda Complex, Mr. Freeman.\n'

    file_content = bytes(body.encode('UTF-8'))
    file_name = key.split('/')[-1]
    s3.put_object(
        Bucket=store_bucket,
        Key=f'processed/{file_name}',
        Body=file_content,
    )
    s3.delete_object(
        Bucket=upload_bucket,
        Key=key,
    )
