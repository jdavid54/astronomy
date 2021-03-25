import requests
from bs4 import BeautifulSoup
from os import path
import pathlib   #python 3.4 or above 
import pandas as pd

if not path.exists("planets_data.csv"):
#file = pathlib.Path("planets_data.csv")
#if file.exists():
    result = requests.get("https://promenade.imcce.fr/fr/pages1/19.html")
    #print(result.status_code)
    #print(result.headers)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    #print(soup)

    links = soup.find_all("tr")
    #print(links)

    table_data = [[cell.text.strip().replace(',','.').replace('\r\n\t\t  ','') for cell in row if cell != '\n'] for row in links]
    '''
    for l in table_data:
        for t in l:
            print(t, end='\t')
        print()

    for n in range(10):
        for l in table_data:
            print(l[n], end=',')
        print()
    '''
    data = pd.DataFrame(table_data)
    print(data[1])  #Mercure
    #Nom de la planète : 1-Mercure, 2-Vénus, 3-Terre, 4-Mars, 5-Jupiter, 6-Saturne, 7-Uranus, 8-Neptune, 9-Pluton(*)
    print(data.loc[:,[0,3]])

    data.to_csv('planets_data.csv')

else:
    data = pd.read_csv("planets_data.csv")
    print(data)

data = pd.read_csv("planets3&4.csv",index_col='0')
print(data)