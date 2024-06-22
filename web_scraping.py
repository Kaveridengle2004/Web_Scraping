import requests
from bs4 import BeautifulSoup as bs

url=input("Enter the Website Url :")

response= requests.get(url)

soup= bs(response.text,"html.parser")

print(soup)