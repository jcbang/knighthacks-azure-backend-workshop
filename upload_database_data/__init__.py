import logging

import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey

# The "main" function expects an input web request, and outputs a web response
def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    This Function expects an input JSON web request, and will create a new entry in the Cosmos Database
    based on the input of this Function

    If you haven't already, PLEASE see the 'local' version of this code in order to get a more verbose
    explanation of what's going on in this Function!
    """

    # Your endpoint is specific to your database, allowing you to access
    # its contents over the internet!
    ENDPOINT = '<ENDPOINT>'

    # Your private key is your unique "password" that grabts you
    # permission to modify your database, DO NOT SHARE THIS KEY!
    KEY = '<KEY>'

    # Initialize your CosmosDB Client, allowing you to use CosmosDB APIs
    cosmos_client = CosmosClient(ENDPOINT, KEY)

    # Initialize your database if it doesn't exist
    database_name = 'demo_database'
    cosmos_database = cosmos_client.create_database_if_not_exists(id = database_name)

    # Initialize your container inside of the database if it doesn't exist
    container_name = 'demo_container'
    cosmos_container = cosmos_database.create_container_if_not_exists(id = container_name, 
        partition_key = PartitionKey(path = '/type'),
        offer_throughput = 400)

    # Get the JSON object you sent over the web
    # Remember, the JSON object requires the 'id' field in order to work properly!
    # Example of a request that will work without error:
    # { 
    #      "id": "123",
    #      "type": "smoothie",
    #      "name": "berry smoothie",
    #      "ingredients": ["blackberry", "strawberry"]
    # }
    object_to_create = req.get_json()

    # Try to create the object in the database using .create_item(object)
    try:
        response = cosmos_container.create_item(body = object_to_create)
        return func.HttpResponse(f'We made an item in the database!', status_code = 200)
    # Catch any errors that might occur
    except:
        return func.HttpResponse(f'Something went wrong :(', status_code = 400)
