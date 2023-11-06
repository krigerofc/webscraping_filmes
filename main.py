import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_itens = soup.find('div', class_='sc-29b01cb5-7 hfMYOI').get_text().strip()[0:3]

itens = soup.find_all('ul', class_=re.compile('ipc-metadata-list ipc-metadata-list--dividers-between sc-9d2f6de0-0 ckQYbL compact-list-view ipc-metadata-list--base'))

dic_produtos = {'nome':[],
                'nota':[],
                'ano':[]}

for i in itens:
    for filme in i:
       nome = filme.find('h3', class_='ipc-title__text').get_text().strip()
       nota = filme.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').get_text()
       ano = filme.find('div', class_='sc-c7e5f54-7 brlapf cli-title-metadata').get_text()[0:4]
       print(f'nome: {nome} | Nota: {nota} | Ano: {ano}')
       dic_produtos['nome'].append(nome)
       dic_produtos['nota'].append(nota)
       dic_produtos['ano'].append(ano)

df = pd.DataFrame(dic_produtos)
df.to_csv('C:/Users/pedro/Downloads/form.csv', encoding='utf-8', sep=';')