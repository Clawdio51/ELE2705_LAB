
import json

from utils.status_codes import STATUS_CODE


def parse_response(response):

    response = json.loads(response)
    response["status"] = STATUS_CODE(response["status"]).name

    return response