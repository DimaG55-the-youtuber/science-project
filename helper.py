import requests
import json
import urllib.parse
key = "AIzaSyCvnxM8LVlSqucFDecBG2Q1dFCZcrSm_Jw"
link = "https://www.googleapis.com/books/v1/volumes?"
def lookup(search):
    query = {"q": search, "key": key}
    query = urllib.parse.urlencode(query)
    return requests.get(f"{link}{query}")

def bss_code(categories):
    cat = categories[:3].upper()