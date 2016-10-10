import requests
from bs4 import BeautifulSoup


page = 1
url = 'https://www.congress.gov/members?q=%7B%22congress%22%3A%22114%22%7D&pageSize=250&page={}'.format(page)

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')


for i in soup.find_all(class_='expanded'):
    for name in i.find(class_='result-heading'):
        print(name.text.split())
        print(name['href'].split('/')[-1])
    for s in i.find_all(class_='result-item')[:3]:
        print(s.text.split())
    print()
