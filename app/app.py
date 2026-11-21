import json
from datetime import datetime, timezone


def lambda_handler(event, context):
    try:
        body = event.get('body', '{}')
        if isinstance(body, str):
            body = json.loads(body)
        if not isinstance(body, dict) or not isinstance(body.get('message'), str):
            return response(400, {'error': 'Field message must be a string'})
        result = {
            'word_count': len(body['message'].split()),
            'timestamp': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
        }
        return response(200, result)
    except (json.JSONDecodeError, TypeError, AttributeError):
        return response(400, {'error': 'Invalid JSON body'})


def response(status, data):
    return {
        'statusCode': status,
        'headers': {'Content-Type': 'application/json; charset=utf-8'},
        'body': json.dumps(data, ensure_ascii=False)
    }
