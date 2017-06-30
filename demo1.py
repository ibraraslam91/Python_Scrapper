import urllib.request
from bs4 import BeautifulSoup

url = urllib.request.urlopen('https://www.olx.com.pk/mobiles-tablets/').read()
links = []
soup = BeautifulSoup(url, 'lxml')
a_link = soup.find_all('a',{'class':'marginright5 link linkWithHash detailsLink'})
cats = soup.find_all('small',{'class':'breadcrumb small'})
for a,c in zip(a_link,cats):
    links.append([a.get('href'),c.text.strip().split('\n')[0].split('»')])
print(links)


