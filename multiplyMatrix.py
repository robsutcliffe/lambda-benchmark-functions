import numpy as np
import json

def matrix_multiply(matrix_a, matrix_b):
    a = np.array(matrix_a)
    b = np.array(matrix_b)
    return np.dot(a, b).tolist()

def handler(event, context):
    matrix_a = event.get('matrix_a')
    matrix_b = event.get('matrix_b')

    if not matrix_a or not matrix_b or len(matrix_a) != len(matrix_a[0]) or len(matrix_b) != len(matrix_b[0]):
        return {"statusCode": 400, "body": "Invalid input matrices"}

    result = matrix_multiply(matrix_a, matrix_b)
    return {"statusCode": 200, "body": json.dumps(result)}
