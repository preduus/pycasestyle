import re
from unidecode import unidecode


def clear_string(text: str):
    text = unidecode(text)
    return re.sub(r'[^a-zA-Z0-9]+', ' ', text)


def split_string(regex, text: str):
    return re.split(regex, text)


def replacement(regex, text: str, replace_to:str = "_"):
    return re.sub(regex, replace_to, text)
