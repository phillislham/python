from pprint import pprint
from datetime import datetime
import json
import boto3
from botocore.config import Config


def get_boto_client():
    config_lambda = Config(retries={'total_max_attempts': 1}, read_timeout=1200)
    return boto3.client(
            'lambda',
            config=config_lambda,
            # en mac
            endpoint_url='http://host.docker.internal:3050',
            # en windows
            # endpoint_url='http://localhost:3050',
            use_ssl=False,
            verify=False,
        )


def fn_a(event, context):
    pprint("fn_a ini")
    now = datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S")
    eventjson = json.dumps(event)

    try:
        response = get_boto_client().invoke(
            FunctionName="MyFunctionB",
            InvocationType='RequestResponse',
            #LogType='Tail', # no va en local
            Payload=json.dumps({"from": "This is some payload for Lambda B"})
        )
    except Exception as ex:
        ex = str(ex)
        return {
            "error": f"Error invoking Lambda B: {ex}"
        }

    if response['StatusCode'] == 200:
        payload = json.loads(response['Payload'].read())
        pprint(payload)
        if "error" in payload:
            return {
                "error": f"Error response from Lambda B: {payload['error']}"
            }
        return {
            "event": f"input event:\n {eventjson}",
            "success": f"This is a response succes from Lambda A {now}",
            "from-lambda-b": f"{payload['success']}"
        }
    else:
        return {
            "error": f"Error in response from Lambda B status: {response['StatusCode']}"
        }


