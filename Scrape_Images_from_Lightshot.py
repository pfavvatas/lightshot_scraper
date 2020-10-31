import requests
from bs4 import BeautifulSoup
import shutil
import random
from datetime import datetime
import time
from pathlib import Path


import cloudscraper

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session

rundomList = ["0","1","2","3","4","5","6","7","8","9"
              ,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

originalText = "https://prnt.sc/"
d = datetime.now().strftime("%m%d%Y%H%M%S")
print(d)
dd = str(d)
Path("img/"+dd).mkdir(parents=True, exist_ok=True)
while True:
    rundomFullText = random.choice(rundomList) + random.choice(rundomList) + random.choice(rundomList) + random.choice(rundomList) + random.choice(rundomList) + random.choice(rundomList)
    newText = originalText + rundomFullText
    html = scraper.get(newText).text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    image_url = soup.find('img')['src']
    if image_url[0] == '/':
        continue
    else:
        print(image_url)
        resp = requests.get(image_url, stream=True)
        local_file = open('img/'+dd+'/'+rundomFullText+'.png', 'wb')
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, local_file)
        del resp    