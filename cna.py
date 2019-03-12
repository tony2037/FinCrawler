import requests
from bs4 import BeautifulSoup

url = 'https://www.cna.com.tw/list/aie.aspx'
target = []

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
sel = soup.select('ul#myMainList li a')
for s in sel:
    href = s['href']
    if (href.find('https') != -1 or href.find('http') != -1):
        target.append(href)
        print(href)
