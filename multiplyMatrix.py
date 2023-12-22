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
    matrix_size_str = event['queryStringParameters']['matrix_size']
    matrix_size = int(matrix_size_str)

    if not matrix_size:
        return {"statusCode": 400, "body": "matrix_size not received"}

    matrix_a, matrix_b = generate_matrices(matrix_size)

    result = matrix_multiply(matrix_a, matrix_b)

    cors_headers = {
        "Access-Control-Allow-Origin": "https://robsutcliffe.static.observableusercontent.com",
        "Access-Control-Allow-Methods": "GET"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps({ "success": "true" }),
        "headers": cors_headers
    }

    return response
