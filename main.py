import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from time import sleep

table = PrettyTable()
table.field_names = ['GameName','GameLink']

def main(PageId):
    request = requests.get(f'https://torrent-igruha.org/newgames/page/{PageId}/')
    page = BeautifulSoup(request.content, 'html.parser')
    MainBlock = page.find('div',class_='articles-film-cuted')
    GameBlocks = MainBlock.findAll('div',class_='article-film')
    for GameBlock in GameBlocks:
        GameName = (GameBlock.find(class_='article-film-title')).text
        GameLink = ((GameBlock.find(class_='article-film-title')).find('a'))['href']
        table.add_row([GameName,GameLink])
    
for i in range(1,95):
    main(i)
open('Table.txt','a').write(str(table))
#Fdfgdf
