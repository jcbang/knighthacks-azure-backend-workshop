import logging

import azure.functions as func

# This is what an Azure Function looks like after it was just created!
# The "main" function expects an input web request, and outputs a web response
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # If you're confused by all of this code, that's okay!
    # I have a cleaner, commented sample Azure Function called "simple_test_function" that you should take a look at :)

    # I just left this in here so you are aware that this is the expected auto-generated code that appears when
    # you make a new Function
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
