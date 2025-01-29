"""
Scrapping data from a stock website marketwatch.com of Apple stock
"""
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.marketwatch.com/search?q=apple&ts=0&tab=All%20News')
# print(page)
soup = BeautifulSoup(page.text, 'lxml')
# print(soup)

# Scrape the current price of stock which is Big One
price = soup.find('big-quote', class_='value').text
print(price)

# Scrape previous closed price
closed_price = soup.find('td', class_='table_cell i-semi').text
print(closed_price)

# Scrape 52 week range prices(lower & upper)
lower = soup.find('span', class_='primary').text
# but if you get another instance than the one you need then you need to know that with the same TAG & CLASS we have
# another HTML. So in this case you need to get the required one by taking the help of PARENT TAG or NESTED TAG
# (which is called extracting HTML elements from nested HTML Tags as below)
parent_tag = soup.find('mw-regular', class_='element element--range range-yearly')
lower_price = parent_tag.find_all('span', class_='primary')[0].text
upper_price = parent_tag.find_all('span', class_='primary')[1].text

# Scrape analyst rating
rating = soup.find('li', class_='analyst_option active').text
print(rating)

# Tip: May be the stock prices data from company to company will change, but the backgroung core HTML elements
# (Tags, class names etc.,) will not change.
