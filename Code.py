import requests
import pyttsx3
import json

query=input("What type of news are you interested in?")
url=f"https://newsapi.org/v2/everything?q={query}&from=&sortBy=publishedAt&apiKey=dc3ab12015dc44098d5928f620a8e923"
r=requests.get(url)
news=json.loads(r.text)

engine=pyttsx3.init()

def reading():
    for article in news["articles"]:
         
         print(article["title"])
         print(article["description"])
         print("-----------------------------")


reading()
