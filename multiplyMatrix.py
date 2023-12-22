import numpy as np
import random
import json

def generate_matrices(matrix_size):
    matrices = [[[random.random() for _ in range(matrix_size)] for _ in range(matrix_size)],
                [[random.random() for _ in range(matrix_size)] for _ in range(matrix_size)]]
    return matrices
def matrix_multiply(matrix_a, matrix_b):
    a = np.array(matrix_a)
    b = np.array(matrix_b)
    return np.dot(a, b).tolist()

def handler(event, context):
    body = json.loads(event['body'])

    matrix_size = body.get('matrix_size');

    if not matrix_size:
        return {"statusCode": 400, "body": "matrix_size not received"}

    matrix_a, matrix_b = generate_matrices(matrix_size)

    result = matrix_multiply(matrix_a, matrix_b)

    cors_headers = {
        "Access-Control-Allow-Origin": "https://robsutcliffe.static.observableusercontent.com",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "POST"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(result),
        "headers": cors_headers
    }

    return response
