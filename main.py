import requests
from fastapi import FastAPI
from method import *
import whois

app = FastAPI()


@app.get("/api/checker-tools/ip_lookup/{ip_address}")
async def ip_lookup(ip_address: str):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    return data


@app.get("/api/teks-tools/teks-separator/{teks}")
async def whois_lookup(teks: str):
    response = teks_separator(teks)
    return response


