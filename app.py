import requests
from bs4 import BeautifulSoup

url = 'http://jadwalsholat.pkpu.or.id/monthly.php?id=142'
content = requests.get(url)
#print(content.text)

soup = BeautifulSoup(content.text, 'html.parser')
data = soup.find_all( 'tr', 'table_highlight')
data = data[0]

solat= {}
i=0
for d in data:
    if   i == 1:
        solat['subuh'] = d.get_text
    elif i == 2:
        solat['dhuhur'] = d.get_text()
    elif i == 3:
        solat['ashar'] = d.get_text()
    elif i == 4:
        solat['magrib'] = d.get_text()
    elif i == 5:
        solat['isya'] = d.get_text()
    i +=1
print(solat)
