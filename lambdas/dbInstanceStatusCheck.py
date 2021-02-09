import boto3

def lambda_handler(event, context):
    
    client = boto3.client('rds',region_name='us-west-2')
    response = client.describe_db_instances(
    DBInstanceIdentifier='agniv-db'
    )
    
    for i in response['DBInstances']:
        db_status = i['DBInstanceStatus']
        db_endpoint_address = i['Endpoint']['Address']
        
    if db_status !='available':
        print('database endpoint is not available yet ..')
    

    if db_status=='available':
        print('database endpoint is available for cname switch')
        print('endpoint is : ' + db_endpoint_address)
        
    return {
        "db_status": db_status,
        "db_endpoint_address": db_endpoint_address
        } 