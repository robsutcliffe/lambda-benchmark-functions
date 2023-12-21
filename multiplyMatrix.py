import numpy as np
import json

def matrix_multiply(matrix_a, matrix_b):
    a = np.array(matrix_a)
    b = np.array(matrix_b)
    return np.dot(a, b).tolist()

def handler(event, context):
    body = json.loads(event['body'])

    matrix_a = body.get('matrix_a')
    matrix_b = body.get('matrix_b')

    if not matrix_a or not matrix_b:
        return {"statusCode": 400, "body": "matrices not received"}

    if len(matrix_a) != len(matrix_a[0]):
        return {"statusCode": 400, "body": "matrices should be same length"}

    if len(matrix_b) != len(matrix_b[0]):
        return {"statusCode": 400, "body": "matrices are not same length and breadth"}

    result = matrix_multiply(matrix_a, matrix_b)

    cors_headers = {
        "Access-Control-Allow-Origin": "https://robsutcliffe.static.observableusercontent.com",
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Access-Control-Allow-Methods": "DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(result),
        "headers": cors_headers
    }

    return response
