"""
Open Google Chrome & type top 100 movies of all time
Press ENTER and click on the link corresponding to imdb
Create a wait time for the entire page to load
Scroll all the way to down until you see Jawn movie
Take a screenshot of that page & also take screenshot of the Jawn movie poster
Mostly using XPATH rather than others since sometimes it'll show unabletofindelement error
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


# Starts our driver and goes to the starting webpage which is google.com
driver = webdriver.Chrome()
driver.get('https://google.com')

# Inputs text into the google search box
search = driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search.send_keys('top 100 greatest movies of all time imdb')

# Presses the enter button to search
search.send_keys(Keys.ENTER)
time.sleep(2)

# Presses on the link for Imdb
driver.find_element(By.XPATH, '//*[@id="rso"]/div[2]/div/div[1]/a/h3').click()

# 3second wait time to let the entire page load in
time.sleep(3)

# Scrolls until Jaws the movie is on the screen
driver.execute_script('window.scrollTo(0,22500)')

# Takes a screenshot of the webpage
driver.save_screenshot('C:\Web Scraping course\jaws.png')

# Takes a screenshot of the Jaws movie poster
driver.find_element(By.XPATH, '//*[@id="main"]/div/div[4]/div[3]/div[50]/div[1]/a/img').screenshot('C:\Web Scraping course\jaws2.png')
