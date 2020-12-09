import json


def lambda_handler(event, context):
    # TODO implement
    response = {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

    # GET handler
    if (event["httpMethod"] == "GET"):
        response = {
            'statusCode': 200,
            'body': json.dumps('Hello from GET Lambda')
        }

    # POST handler
    if (event["httpMethod"] == "POST"):
        response = {
            'statusCode': 200,
            'body': json.dumps('Hello from POST Lambda')
        }

    return response
