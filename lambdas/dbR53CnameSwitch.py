import boto3

def lambda_handler(event, context):
    
    client = boto3.client('route53')
    db_endpoint = event['db_endpoint_address']

    response = client.change_resource_record_sets(
    HostedZoneId='Z01463142843JVI1JBFSU',
    ChangeBatch={
        'Comment': 'Updating R53 record for the db instnace',
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': 'agniv-db-proto.testdomain.com',
                    'Type': 'CNAME',
                    'TTL': 300,
                    'ResourceRecords': [
                        {
                            'Value': db_endpoint
                        },
                    ]
                }
            },
        ]
    }
    )
    print('Db instnace cname switch initiated')