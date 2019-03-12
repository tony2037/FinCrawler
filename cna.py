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
for n in target:
    news = requests.get(n)
    soup = BeautifulSoup(news.text, 'html.parser')
    title = soup.select('h1')
    time = soup.select('div.timeBox div.updatetime span')
    content = soup.select('p')
    print('Titile: %s' % title[0].text)
    print('Time: %s' % time[0].text)
    print('Content: ')
    for c in content:
        print(c.text)
    print('=' * 15)
