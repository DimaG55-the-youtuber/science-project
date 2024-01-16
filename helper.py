import requests
import json
import urllib.parse
key = "AIzaSyCvnxM8LVlSqucFDecBG2Q1dFCZcrSm_Jw"
link = "https://www.googleapis.com/books/v1/volumes?"
def lookup(search):
    query = {"q": search, "key": key}
    query = urllib.parse.urlencode(query)
    print(f"{link}{query}")
    return requests.get(f"{link}{query}")