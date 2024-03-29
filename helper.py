import requests
import urllib.parse
import random
key = "AIzaSyCvnxM8LVlSqucFDecBG2Q1dFCZcrSm_Jw"
link = "https://www.googleapis.com/books/v1/volumes?"
def lookup(search):
    query = {"q": search, "key": key}
    query = urllib.parse.urlencode(query)
    return requests.get(f"{link}{query}")

def bss_code(categories):
    cat = categories.replace(" ", "_").upper()
    row = "{:03d}".format(random.randint(1, 100))
    shelf = random.randint(1, 9)
    identify = "{:03d}".format(random.randint(1, 100))
    return f"{cat}.{row}.{shelf}.{identify}"
