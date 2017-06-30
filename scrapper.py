import urllib.request
from bs4 import BeautifulSoup
from multiprocessing import Pool
import numpy as np
import pandas as pd

cats = {
        'Bikes':17,
        'Motorcycles':18,
        'Spare Parts':19,
        'Bicycles':20,
        'Scooters':21,
        'ATV & Quads':22
        }

def get_links(url_in):
    url = urllib.request.urlopen(url_in).read()
    links = []
    soup = BeautifulSoup(url, 'lxml')
    a_link = soup.find_all('a', {'class': 'marginright5 link linkWithHash detailsLink'})
    add_cats = soup.find_all('small', {'class': 'breadcrumb small'})
    for a,cat in zip(a_link,add_cats):
        catss = cat.text.strip().split('\n')[0].split('»')
        try:
            cat1 = cats[catss[0].strip()]
        except:
            cat1 = 0
        try:
            cat2 = cats[catss[1].strip()]
        except:
            cat2 = 0
        if (cat2>cat1):
            links.append([a.get('href'),cat2])
        else:
            links.append([a.get('href'), cat1])
    return links
base_url = 'https://www.olx.com.pk/bikes/?page='
pages = []
pages.append('https://www.olx.com.pk/bikes/')
for i in range(2,501):
    pages.append(base_url+str(i))
pool = Pool(10)
a_links = pool.map(get_links,pages)
total_successes = [ent for sublist in a_links for ent in sublist]
nn = np.array(total_successes)
column = ['href', 'cat']
file_name = 'data.csv'
df = pd.DataFrame(nn,columns=column)
df.to_csv(file_name,index=False)