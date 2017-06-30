import requests


insert_url = 'http://localhost/wp/demo2.php'
title = "POST DEMO 2"
content = "POST CONTENT 2"
file = "https://apollo-singapore.akamaized.net/v1/files/bb2sdkvneb18-PK/image;s=1000x700;pk_;slot=1;filename=bb2sdkvneb18-PK_.jpg"

data = {'title':title,'content':content,'file':file}
r = requests.post(insert_url,data=data)
print(r.text)