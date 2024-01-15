import requests
import urllib.parse
key = "AIzaSyCvnxM8LVlSqucFDecBG2Q1dFCZcrSm_Jw"
query = {"q": input("Book: "), "key": key}
link = "https://www.googleapis.com/books/v1/volumes?"
query = urllib.parse.urlencode(query)
print(f"{link}{query}")
book_search = requests.get(f"{link}{query}")
# print(book_search.text)