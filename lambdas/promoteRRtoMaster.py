import boto3

def lambda_handler(event, context):
    
    client = boto3.client('rds',region_name='us-west-2')
    response = client.promote_read_replica(
    DBInstanceIdentifier='agniv-db'
    )
    print('Read Replica promotion to Master initiated')