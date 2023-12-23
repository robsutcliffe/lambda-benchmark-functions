import numpy as np
import json

def generate_matrices(matrix_size):
    return [np.random.rand(matrix_size, matrix_size) for _ in range(2)]

def matrix_multiply(matrix_a, matrix_b):
    a = np.array(matrix_a)
    b = np.array(matrix_b)
    return np.dot(a, b).tolist()

def handler(event, context):
    cors_headers = {
        "Access-Control-Allow-Origin": "https://robsutcliffe.static.observableusercontent.com",
        "Access-Control-Allow-Methods": "GET"
    }

    if event.get('queryStringParameters', {}).get('ping') == 'true':
        return {
            "statusCode": 200,
            "body": "pong",
            "headers": cors_headers
        }

    matrix_size_str = event['queryStringParameters']['matrix_size']
    matrix_size = int(matrix_size_str)

    if not matrix_size:
        return {"statusCode": 400, "body": "matrix_size not received"}

    matrix_a, matrix_b = generate_matrices(matrix_size)

    result = matrix_multiply(matrix_a, matrix_b)

    response = {
        "statusCode": 200,
        "body": json.dumps({ "success": "true" }),
        "headers": cors_headers
    }

    return response
