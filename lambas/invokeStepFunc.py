import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('stepfunctions')
    response = client.start_execution(
        stateMachineArn='arn:aws:states:us-east-1:159184006576:stateMachine:DbPromoteRRtoMaster'
    )
    print('Step Function invoked..')