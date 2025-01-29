"""
Scraping a Table from World population website
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'
page = requests.get(url)
# print(page)
soup = BeautifulSoup(page.text, 'lxml')
# print(soup)

parent_tag = soup.find('table', class_='table table-striped table-bordered table-hover table-condensed table-list')
# print(table_tag)
columns = []
for i in parent_tag.find_all('th'):
    columns.append(i.text)
print(columns)

rows = []
for j in parent_tag.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [a.text for a in row_data]  # if we see any white spaces on both sides of the element the a.text.strip()
    rows.append(row)
print(rows)

# Display options to show all the rows & columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.DataFrame(data=rows, columns=columns)
df.to_csv('/Users/mohansai/Documents/bs4_worldpop_project.csv')
print(df)

# If we want to do some cleaning activity that means removing spaces & taking a part of that tag
# (I mean taking fullname only not even logo or some short names) for a single tag for example for 'td' tag
for j in parent_tag.find_all('tr')[1:]:
    first_td = j.find_all('td')[0].find('div', class_='d3-o-club-fullname').text.strip()
    row_data = j.find_all('td')[1:]
    row = [a.text.strip() for a in row_data]
    row.insert(0, first_td)
    rows.append(row)
