#Direct Bids Web Scraper


#Import Plugins
import requests
from bs4 import BeautifulSoup
from csv import writer
import uuid
import time

i=0

while i <= 0:           #0 = number of loops +1  or  #0 = number of pages +1
 i = i + 1   
 print(i)
 time.sleep(5)

 response = requests.get("https://www.directbids.com/auctions?categories=775856496&page=" + str(i))           #Link Goes Here
 soup = BeautifulSoup(response.text, 'html.parser')
 posts = soup.find_all("div", {"class": "grid-item"})

 print('Stage 1')

 filename = str(uuid.uuid4())
 print(filename)

 with open('DirectBidsAuction' + filename + '.csv', 'w' ) as csv_file:                #File Name
     csv_writer = writer(csv_file)
     headers = ['Lot', 'Info', 'Photo', 'Bid', 'Title']
     csv_writer.writerow(headers)

     for post in posts:
        print('Stage 2')

        Lot = post.find_all(class_='d-flex mb-1 small mb-2')
        print(Lot)

        Info = post.find('a')['href']      #
        print(Info)

        Photo = post.find(class_='grid-item-img')['src']        #
        print(Photo)

        Bid = post.find_all(class_='d-flex mb-1')
        print(Bid)

        Title = post.find(class_='grid-item-title')
        print(Title)

        csv_writer.writerow([Lot, Info, Photo, Bid, Title])
print('Stage 3')