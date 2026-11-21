import json
from flask import Flask, request, Response
from app.app import lambda_handler

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return {'status': 'running'}
    result = lambda_handler({'body': request.get_data(as_text=True)}, None)
    return Response(result['body'], status=result['statusCode'], content_type='application/json; charset=utf-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
