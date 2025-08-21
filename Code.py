import requests
import pyttsx3
import json

query=input("What type of news are you interested in?")
url=f"https://newsapi.org/v2/everything?q={query}&from=&sortBy=publishedAt&apiKey=your_api_key"
r=requests.get(url)
news=json.loads(r.text)

engine=pyttsx3.init()

def reading():
    for article in news["articles"]:
         
         print(article["title"])
         print(article["description"])
         print("-----------------------------")

reading()


def speak():
     engine.say(str(news))

ask=input("Do you want to Hear News")

if ask=="Yes" or "yes":
     speak()
elif ask=="No" or "no":
     print("Okay , No problem ")
else:
     print("Thanks for the answer")
     


engine.runAndWait()

     







 
      
