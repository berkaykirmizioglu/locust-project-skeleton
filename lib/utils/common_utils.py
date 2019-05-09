from bs4 import BeautifulSoup


def get_token(response_text) -> str:
    """Parses CSRF Token value from response html of request.
    :param response_text:
    :return: Returns parsed CSRF Token value.
    """
    soup = BeautifulSoup(response_text, features="html.parser")
    token = soup.find(attrs={"name": "token"})
    return token['value']
