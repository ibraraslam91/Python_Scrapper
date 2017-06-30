import urllib.request
from bs4 import BeautifulSoup

url = urllib.request.urlopen('https://www.olx.com.pk/item/need-a-samsung-galaxy-5280-or-5280-IDWfFYv.html#75c647931c').read()

soup = BeautifulSoup(url, 'lxml')
div = soup.find('div',{'class':'photosbar'})
image = div.find('a',{'class':'block br5 {nr:1}'})
price = soup.find('strong',{'class':'xxxx-large margintop7 block not-arranged'}).text.strip()
title = soup.find('h1',{'class':'brkword lheight28'}).text.strip()
location = soup.find('span',{'class':'show-map-link link gray cpointer'}).text.strip()
person = soup.find('span',{'class':'block color-5 brkword xx-large'}).text.strip()
phone = soup.find('strong',{'class':'large lheight20 fnormal  '}).text.strip()
dec = soup.find('p',{'class':'pding10 lheight20 large'}).text.strip()





