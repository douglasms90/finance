from flask import Flask, render_template
from urllib.request import urlopen
from bs4 import BeautifulSoup


app = Flask(__name__)

url = "https://www.infomoney.com.br/mercados/renda-fixa"
html = urlopen(url)
bs = BeautifulSoup(html, 'html')
cdi = bs.find('li', class_='li-cdi').find('strong').get_text().split('%')

@app.route('/')
@app.route('/home')
def home():
  return render_template("home.html", info = cdi)