from bs4 import BeautifulSoup
import requests

base_url='https://quotes.toscrape.com/'
response=requests.get(base_url)
soup=BeautifulSoup(response.text,'html.parser')

quotes=soup.find_all('span',class_='text')
authors=soup.find_all('small',class_='author')

for q,a in zip(quotes,authors):
    print(f'{q.text} - {a.text}')