import logging
import json

import azure.functions as func

# The "main" function expects an input web request, and outputs a web response
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # In this example, the expected HttpRequest has a JSON body,
    # we can access that by the line of code below
    # req_body is a Python dictionary object that is created based on the JSON input we passed into the function
    req_body = req.get_json()

    # If we sent a POST request to this function that looked like this:
    # {
    #     "key1": "val1",
    #     "key2": "val2",
    # }
    # Then we can access those variables with the following Python code:
    # print(req_body['key1']) -> prints 'val1'
    # print(req_body['key2']) -> prints 'val2'

    # For reference, json.dumps(req_body) converts the Python object req_body back into a JSON string
    return func.HttpResponse(f'Yay! We have a successful response! This was the input: {json.dumps(req_body)}', status_code = 200)
