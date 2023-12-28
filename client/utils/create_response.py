import json


def create_response(response):

    response_copy = {}
    for k in response.keys():
        response_copy[k] = response[k]

    response_copy["status"] = response_copy["status"].value

    return json.dumps(response_copy)