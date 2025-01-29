"""
BeautifulSoup concepts
"""
import re
import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
page = requests.get(url)
print(page.text)

soup = BeautifulSoup(page.text, 'lxml')
print(soup)

# HTML elements
# Tags: which are in purple colour
print(soup.header)

# Navigable string
# To access Navigable string in a nested tag in a string(which is in black colour) format then
print("\n")
print(soup.header.p.string)

# Attributes: which are in yellow colour
print(soup.header.a.attrs)

# find: Used to get HTML based on tags, attributes which will give the first occurrence
soup.find('header') and soup.header  # are same
soup.find('dev', {'class': 'pull-right price'}) and soup.find('dev', class_='pull-right price')  # are same
# where dev is the tag

# find_all: Used to get HTML based on tags, attributes which will give all the occurrences from the entire HTML
# as a list, yes it supports indexing & slicing :)
x = soup.find_all('dev', {'class': 'pull-right price', 'id': 'side-menu'})[2]

# Based on multiple tags
soup.find_all(['dev', 'h'])

# To get all the lines of HTML code which has an ID attribute
soup.find_all(id=True)

# To get all the occurrences of a string in HTML code which will give as a List.
soup.find_all(string='Iphone')  # ['Iphone', 'Iphone', 'Iphone']

# BeautifulSoup also supports reqular expressions with String & attributes
soup.find_all(string=re.compile('Iph'))  # ['Iphone', 'Iphone', 'Iphone']
soup.find_all(string=re.compile('Nok'))  # ['Nokia', 'Nokia 45']
soup.find_all(string=['Nokia 123', 'Iphone'])  # ['Iphone', 'Iphone', 'Nokia 123']
soup.find_all(class_=re.compile('pull'))  # ['pull-right price', 'pull-on']
soup.find('dev', class_=re.compile('pull'))  # gives all occurrences but no need to give complete class
soup.find('dev', class_=re.compile('pull'), limit='3')
