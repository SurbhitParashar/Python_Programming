#it get the current news from the news api and print the news
import requests
import json

class newsapp:
    def __init__(self,opt):
        self.option=opt
    
    def get_info(self,url):
        news=json.loads(url.text)
        for article in news["articles"]:
            print(article["title"])
            print(article["description"])
            print("----------------------------------")
            
    def info(self):
        if self.option==1:
            url=requests.get("https://newsapi.org/v2/everything?q=tesla&from=2024-06-19&sortBy=publishedAt&apiKey=d6245a0e7c35435ab4d55f5523789dfe")
            self.get_info(url)   
        elif self.option==2:
            url=requests.get("https://newsapi.org/v2/everything?q=apple&from=2024-07-18&to=2024-07-18&sortBy=popularity&apiKey=d6245a0e7c35435ab4d55f5523789dfe")
            self.get_info(url)
        elif self.option==3:
            url=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=d6245a0e7c35435ab4d55f5523789dfe")
            self.get_info(url)
        else:
            exit()

def option():
    print("1. Sports News"
            "2. Politics News"
            "3. Hollywood News"
            "4. Quit ")
    opt=int(input("enter from the above choices : "))
    return opt
        
print("****************** Welcome to NewsApp ******************")
a=option()
newsapi=newsapp(a)
newsapi.info()
