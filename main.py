import requests
from bs4 import BeautifulSoup as bs

site = 'https://eksisozluk.com/'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
while True:
    baslik= input('Baslik: ')
    if baslik == 'exit':
        break

    r = requests.get(site + baslik, headers=header)

    if r.status_code != 200:
        print('Bulamadım')
    else:
        soup = bs(r.content, 'html.parser')
        entryler = soup.find(id='entry-item-list').find_all('li')

        #entryler[0].find(class_ = 'content').get_text(Strip=True)
        #entryler[0].find(class_ ='entry-date').get_text(strip=True)
        #entryler[0].find(class_ ='entry-author').get_text(strip=True)

        print('-'*20, 'ENTRYLER', '-'*20, sep='\n')
        for num, entry in enumerate(entryler, 1):
            yazar = entry.find(class_='entry-author').get_text(strip=True)
            tarih = entry.find(class_='entry-date').get_text(strip=True)
            icerik = entry.find(class_='content').get_text(strip=True)

            print('{}. {} \n\nyazar:{}, tarih: {}'.format
                  (num, icerik, yazar, tarih)
                  )
            print('='*25)