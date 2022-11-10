import requests
from requests import Response


def dict_api_request(search_word: str) -> Response:
    """Input string is used to for an API request to a Dictionary API.

    :parameter:
            search (str): user provided string used for the payload.
    :returns:
            (Response): Response object containing word definition from Dictionary API request.
    """
    api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    payload = f"{api_url}{search_word}"
    response = requests.get(payload)
    return response


