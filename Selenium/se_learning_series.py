# The selenium.webdriver module provides all the WebDriver implementations(Firefox, Chrome, IE and Remote).
from selenium import webdriver

# The By class is used to locate elements within a webpage.
from selenium.webdriver.common.by import By

# The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium.webdriver.common.keys import Keys

# Convenience methods provided that help you write code that will wait only as long as required.
# WebDriverWait in combination with ExpectedCondition is one way this can be accomplished.
# WAIT makes WebDriver wait for a certain condition to occur before proceeding further steps in the code.
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Action chains in Selenium are used to perform complex user interactions such as mouse movements, key presses,
# and other advanced actions like clicking and holding, double-clicking, or dragging and dropping.
# These actions can simulate real user behavior, which is especially useful in web scraping scenarios
# where simple clicks or inputs aren't sufficient.
# Action Chain is used to perform a predefined list of actions in a sequence manner
from selenium.webdriver.common.action_chains import ActionChains

import time

# Creating a webdriver
# path = '/Users/mohansai/Downloads/chromedriver-mac-arm64/chromedriver'
# service = Service(path)
driver = webdriver.Chrome()
driver.maximize_window()

# Navigating to a link using WebDriver
driver.get("https://www.techwithtim.net/")

# locating elements using By class
# By. ID or NAME or CLASS_NAME or TAG_NAME or XPATH or LINK_TEXT or PARTIAL_LINK_TEXT or CSS_SELECTOR
search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("test")
# This will clear all of the text that's already inside the input field to make sure that empty
search.clear()
search.send_keys("python")
search.send_keys(Keys.RETURN)

# Waits
# to print the content of the SEARCHED_PAGE by ID=main
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # to print all the titles of each article header which are under main tag in the SEARCHED_PAGE then we need to get
    # into each article using loop & print header by class_name=entry-title
    articles = main.find_elements(By.TAG_NAME, "article")
    for article in articles:
        header = article.find_element(By.CLASS_NAME, "entry-title")
        print(header.text)
finally:
    driver.quit()

# To get better clarification, we’ll go through a task that from the Home page, we need to click on the
# Python Programming link text. Then again we need to click on Beginner Python Tutorials and then we need to
# click on Get Started using find_element_by_link_text and link.click().
link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()  # then we need to wait driver for sometime to load the page
try:
    # wait for 10 secs to get the presence of `Beginner Python Tutorials` element located then click it
    element1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element1.click()
    # wait for 10 secs to get the presence of `Get Started` element located by ID then click it
    element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-24526427"))
    )
    element2.click()

    # To navigate back to the before pages
    driver.back()
    driver.back()
    driver.back()
    # To navigate forward to the next pages
    driver.forward()
finally:
    driver.quit()

# Action Chains: used to perform a predefined list of actions in a sequence manner
# Creating an Action Chain object
action = ActionChains(driver)

# Clicking
# Single Click:
element = driver.find_element(By.ID, "element_id")
action.click(element).perform()
# Right Click (Context Click)
action.context_click(element).perform()
# Double Click
action.double_click(element).perform()

# Mouse Hover
# Hovering over an element
action.move_to_element(element).perform()

# Dragging and Dropping
# Drag and Drop by Target
source = driver.find_element(By.ID, "source_id")
target = driver.find_element(By.ID, "target_id")
action.drag_and_drop(source, target).perform()

# Drag and Drop by Offset in Selenium's Action Chains allows you to drag an element from its current position
# and drop it at a specific location determined by x and y offsets.
# Offset refers to the distance you want to move the element in terms of pixels:
# x_offset: Number of pixels to move horizontally (positive values move right, negative values move left).
# y_offset: Number of pixels to move vertically (positive values move down, negative values move up).
action.click_and_hold(source).move_by_offset(100, 50).release().perform()

# Click and Hold
# Holding down a mouse button
action.click_and_hold(element).perform()

# Releasing a Held Click
# Releasing the mouse button
action.release(element).perform()

# Key Presses
# Press and Release Keys
action.send_keys(Keys.ENTER).perform()

# pressing modifier keys such as CTRL, SHIFT, ALT, etc., allows you to simulate keyboard interactions
# that involve holding down a key while performing other actions.
# This can be useful in scenarios like:
# Selecting multiple items.
# Opening links in new tabs (e.g., holding CTRL and clicking).
# Typing text in uppercase (holding SHIFT).
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# Combining Actions
# Action chains allow chaining multiple actions together.
action.move_to_element(element).click().send_keys("Text").perform()

# Releasing and Resetting Actions
# Sometimes, you may need to reset the chain if not performing actions immediately
action.reset_actions()

# Action Chains use Cases in Web Scraping #
# Interacting with dropdown menus or tooltips that require hovering.
# Simulating drag-and-drop operations to load dynamic content.
# Handling sliders or scrollable areas.

time.sleep(6)
driver.quit()

# Udemy
# Starts up our Driver and loads up our starting webpage
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.google.com/')

# inputting text into a search box
box = driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
box.send_keys('web scraping')
box.send_keys(Keys.ENTER)

# clicking on a button
button = driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
button.click()
link = driver.find_element(By.XPATH, '//*[@id="rso"]/div[3]/div/div[1]/a/h3').click()
data_scraping = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[1]/a[1]').click()

# taking a screenshot
driver.save_screenshot('C:\Web Scraping course\screenshot.png')  # takes the screenshot of the driver's current page
driver.find_element(By.XPATH, '//*[@id="rso"]/div[3]/div/div[1]/a/h3').screenshot(
    'C:\Web Scraping course\screenshot2.png')  # takes screenshot of the page you have referred using XPATH

# full example - uses inputting text into a box, clicking on a button, and taking a screenshot
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
box = driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
box.send_keys('giraffe')
box.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="hdtb-msb-vis"]/div[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[3]/a[1]/div[1]/img').screenshot(
    'C:\Web Scraping course\giraffe.png')

# self scrolling
driver.execute_script('return document.body.scrollHeight')  # returns the height of the entire current webpage
driver.execute_script('window.scrollTo(0,6000)')  # it'll sroll upto the given 6000 height
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # it'll sroll the entire page.

# wait times
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_condition as EC
# import time
box = driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
box.send_keys('giraffe')
box.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="hdtb-msb-vis"]/div[2]/a').click()

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'cntratet')))


# PROJECT - 1 Mostly using XPATH rather than others since sometimes it'll show unabletofindelement error
# Open Google Chrome & type top 100 movies of all time
# Press ENTER and click on the link corresponding to imdb
# Create a wait time for the entire page to load
# Scroll all the way to down until you see Jawn movie
# Take a screenshot of that page & also take screenshot of the Jawn movie poster

driver = webdriver.Chrome()
driver.get('www.google.com')
search = driver.find_element(By.XPATH, '')
