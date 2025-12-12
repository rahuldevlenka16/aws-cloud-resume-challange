import json
import boto3
import os

dynamo = boto3.resource("dynamodb")
TABLE_NAME = os.environ.get("TABLE_NAME", "visitor-count")
PARTITION_KEY_VALUE = "visitors"

table = dynamo.Table(TABLE_NAME)

def lambda_handler(event, context):
    # Increment count atomically
    response = table.update_item(
        Key={"pk": PARTITION_KEY_VALUE},
        UpdateExpression="ADD #c :inc",
        ExpressionAttributeNames={"#c": "count"},
        ExpressionAttributeValues={":inc": 1},
        ReturnValues="UPDATED_NEW"
    )
    
    new_count = int(response["Attributes"]["count"])
    
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",  # CORS for browser
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS"
        },
        "body": json.dumps({"count": new_count})
    }

