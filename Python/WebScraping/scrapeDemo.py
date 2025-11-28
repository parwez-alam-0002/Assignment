from bs4 import BeautifulSoup
import requests

base_url='https://books.toscrape.com/'

response=requests.get(base_url)

soup=BeautifulSoup(response.text,'html.parser')
a_tag=soup.select('a[title]')
price=soup.find_all('p',class_='price_color')
stock=soup.find_all('p',class_='instock availability')
for p,a,stk in zip(price,a_tag,stock):
    print(f'{a.text} price is {p.text.replace("Â£","£")} stock{' is available.' if stk.text.strip()=='In stock' else 'is not available.'} \n')


