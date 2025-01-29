"""
Scrape the products data from a e-commerce website and converting that into a dataframe using pandas.
"""
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

product_name = soup.find_all('a', class_='title')

price = soup.find_all('h4', class_='price float-end card-title pull-right')

reviews = soup.find_all('p', class_=re.compile('review-count float-end'))

description = soup.find_all('p', class_='description')

product_name_list = []
for i in product_name:
    name = i.string
    product_name_list.append(name)

price_list = []
for i in price:
    price2 = i.string
    price_list.append(price2)

reviews_list = []
for i in reviews:
    reviews2 = i.text
    reviews_list.append(reviews2)

description_list = []
for i in description:
    description2 = i.text
    description_list.append(description2)

# import pdb;pdb.set_trace()
data = {'Product Name': product_name_list,
        'Price': price_list,
        'Reviews': reviews_list,
        'Description': description_list}
df = pd.DataFrame(data)

# Display options to show all the rows & columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print("Here's the Product details table")
print(df)
