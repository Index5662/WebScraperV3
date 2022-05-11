#Proxibid Web Scraper


# we import the class that we need scraping our blog
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

 response = requests.get("https://www.proxibid.com/reLink-Medical-Auctions-LLC/reLink-Surgical-Auction/event-catalog/185473?p=" + str(i))              #link to direct bids auction
 soup = BeautifulSoup(response.text, 'html.parser')
 posts = soup.find_all("div", {"class": "grid-container fluid"})

 print('Stage 1')

 filename = str(uuid.uuid4())
 print(filename)

 with open('Auction997;' + filename + '.csv', 'w' ) as csv_file:                #file name
     csv_writer = writer(csv_file)
     headers = ['Lot', 'Bid', 'Title', 'Info', 'Photo', 'Lot_Description']
     csv_writer.writerow(headers)

     for post in posts:
        print('Stage 2')

        Lot = post.find(class_='lotListNumber').get_text().replace('\n', '')
        print(Lot)

        Bid = post.find(class_='lotStatusValue').get_text().replace('\n', '')
        print(Bid)

        Title = post.find(class_='showVisited responsive-width').get_text().replace('\n', '')
        print(Title)
        
        Info = post.find('a', class_='responsive-width')['href']
        print(Info)

        Photo = post.find('img')['src']
        print(Photo)

        Lot_Description = post.find(class_='lotDesc').get_text().replace('\n', '')
        print(Lot_Description)
        
        csv_writer.writerow([Lot, Bid, Title, Info, Photo, Lot_Description])
print('Stage 3')