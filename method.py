import re

import requests
import json
import whois


def ip_lookup(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    return json.dumps(data)


def teks_separator(teks):
    delimiters = " |,|\.|-|;"

    result = re.split(delimiters, teks)

    return {"teks": result}
