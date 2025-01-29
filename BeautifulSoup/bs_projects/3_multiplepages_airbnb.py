"""
Scraping data from multiple pages from Airbnb website and convert that into a dataframe using pandas & make it csv
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.airbnb.ca'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
print(soup)

df = pd.DataFrame({'Link': [''], 'Title': [''], 'Details': [''], 'Price': [''], 'Rating': ['']})
while True:
    postings = soup.find_all('div', class_='_Bssblpx')
    for post in postings:
        try:  # if we miss anything of the below information from webpage, it's going to throw an error so to handle
            post_link = soup.find('a', class_='_gfo10').get('href')
            post_link_full = 'https://www.airbnb.ca' + post_link
            title = post.find('a', class_='_gfo10').get('aria-label')
            price = post.find('span', class_='_17upghs').text
            rating = post.find('span', class_='_10fgsve').text
            details = post.find_all('div', class_='_kgsfae')[0]  # will get the first line
            df = df.append(
                {'Link': post_link_full, 'Title': title, 'Details': details, 'Price': price, 'Rating': rating}
                , ignore_index=True
            )
        except:
            pass  # We are telling if some info is not available let it be and don't consider that & pass to next post
    next_page_link = soup.find('a', {'aria-label': 'Next'}).get('href')  # href having url link of the arrow button
    if next_page_link:
        next_page_link_full = 'https://www.airbnb.ca' + next_page_link  # full url link along with host of the arrow button
        url = next_page_link_full
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
    else:
        print("No more pages left")
        break

# Saving dataframe as a csv file
df.to_csv('path/to/store/dataframe/airbnb.csv')
