from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://geobretagne.fr/geonetwork/srv/fre/catalog.search#/metadata/2c904997-3f5e-4fd4-b0bb-42570c972f02').text
soup = BeautifulSoup(html_text , 'lxml')
rechercher = soup.find_all('h1')
#print(html_text)
print(rechercher)
