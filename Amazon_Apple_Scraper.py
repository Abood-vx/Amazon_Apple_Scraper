import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv

filecsv = open('AmazonDataapple.csv', 'w', encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://www.amazon.sa/-/en/s?k=apple&qid=1641464871&ref=sr_pg_1'
file = open('AmazonDataapple.json', 'w', encoding='utf8')
file.write('[\n')
data = {}
csv_columns = ['name', 'price', 'img']
for page in range(7):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher = soup.find_all('div', {'class': 'a-section aok-relative s-image-square-aspect'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i = 0
    writer.writeheader()
    for pt in ancher:
        name = pt.find('img', {'class': 'alt'})
        itemPrice = pt.find('span', {'class': 'a-price-whole'})
        img = pt.find('img', {'s-image': 'srcset'})

        if img:
            writer.writerow(
                {'name': name.text.replace('                    ', '').strip('\r\n'), 'price': a-price-whole.text,
                 'img': img.get('s-image')})
            data['name'] = name.text.replace('                    ', '').strip('\r\n')
            data['price'] = itemPrice.text
            data['img'] = img.get('src')
            json_data = json.dumps(data, ensure_ascii=False)
            file.write(json_data)
            file.write(",\n")
file.write("\n]")
filecsv.close()
file.close()