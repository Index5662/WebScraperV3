#Centurion Web Scraper


#Import Plugins
import requests
from bs4 import BeautifulSoup
from csv import writer
import uuid
import time

i=0

while i <= 21:           #0 = number of loops +1  or  #0 = number of pages +1
 i = i + 1   
 print(i)
 time.sleep(1435)

 response = requests.get("https://bid.centurionservice.com/auctions/catalog/id/375?items=50" """+ str(i)""")           #Link Goes Here
 soup = BeautifulSoup(response.text, 'html.parser')
 posts = soup.find_all("li", {"class": "item-block"})
 
 print('Stage 1')

 filename = str(uuid.uuid4())
 print(filename)

 with open('CenturionAuction' + filename + '.csv', 'w' ) as csv_file:            #File name
     csv_writer = writer(csv_file)
     headers = ['Lot', 'Info', 'Photo', 'Bid', 'Asking', 'Title']
     csv_writer.writerow(headers)

     for post in posts:
        print('Stage 2')

        Lot = post.find(class_='auc-lot-link').get_text().replace('\n', '')
        print(Lot)

        Info = post.find('a')['href']
        print(Info)

        Photo = post.find('img')['src']
        print(Photo)

        Bid = post.find(class_='value').get_text().replace('\n', '')
        print(Bid)

        Asking = post.find(class_='item-askingbid').get_text().replace('\n', '')
        print(Asking)

        Title = post.find(class_='yaaa').get_text().replace('\n', '')
        print(Title)
        
        csv_writer.writerow([Lot, Info, Photo, Bid, Asking, Title])
print('Stage 3')