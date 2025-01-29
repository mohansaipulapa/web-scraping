"""
Scraping data from multiple pages(only 10 pages) from carpages website & convert that data into a Dataframe
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.carpages.com'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame({'Link': [''], 'Title': [''], 'Price': [''], 'colour': ['']})

counter = 0
while counter <= 10:
    postings = soup.find_all('div', class_='media-soft push rule')
    for post in postings:
        post_link = post.find('a', class_='media_img---thumb').get('href')
        post_link_full = 'https://www.carpages.ca' + post_link
        Title = soup.find('h4', class_='hN').text.strip()  # if you find any unwanted characters & whitespaces use .strip()
        Price = soup.find('strong', class_='delta').text  # if you find any spaces in class/tag names in HTML, don't worry in soup you don't have those, parser will automatically removes those spaces, so you can give class/tag names without spaces.
        colour = soup.find_all('div', class_='grep1--medium')[1].text.strip()
        df = df.append({'Link': post_link_full, 'Title': Title, 'Price': Price, 'colour': colour})

    next_page_url = soup.find('a', class_='nextprev').get('href')
    page = requests.get(next_page_url)
    soup = BeautifulSoup(page.text, 'lxml')
    counter = counter + 1
