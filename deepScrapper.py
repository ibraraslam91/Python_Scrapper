import pandas as pd
import requests
import urllib.request
from bs4 import BeautifulSoup
from multiprocessing import Pool

hrefs = pd.read_csv('data.csv')
nn = hrefs.as_matrix()
# print(hrefs.shape)
def deepScrap(url):
    try:
        doc = urllib.request.urlopen(url[0]).read()
        soup = BeautifulSoup(doc, 'lxml')
        div = soup.find('div', {'class': 'photosbar'})
        image = div.find('a', {'class': 'block br5 {nr:1}'}).get('href')
        price = soup.find('strong', {'class': 'xxxx-large margintop7 block not-arranged'}).text.strip()
        title = soup.find('h1', {'class': 'brkword lheight28'}).text.strip()
        location = soup.find('span', {'class': 'show-map-link link gray cpointer'}).text.strip()
        person = soup.find('span', {'class': 'block color-5 brkword xx-large'}).text.strip()
        phone = soup.find('strong', {'class': 'large lheight20 fnormal  '}).text.strip()
        dec = soup.find('p', {'class': 'pding10 lheight20 large'}).text.strip()
        insert_url = 'http://45.33.124.188:8080/sdemo.com/inserter.php'
        data = {'title': title,'price':price,'location':location,'person':person,'dec':dec,'phone':phone,'image':image,'cat':url[1]}
        r = requests.post(insert_url, data=data)
        print(r.text)
    except:
        pass
pool = Pool(10)
pool.map(deepScrap,nn)