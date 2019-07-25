from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.infomoney.com.br/mercados/renda-fixa"
html = urlopen(url)
bs = BeautifulSoup(html, 'html')
print(bs.find('li', class_='li-cdi').find('strong').get_text())