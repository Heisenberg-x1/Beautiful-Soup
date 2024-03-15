from selenium import webdriver
from bs4 import  BeautifulSoup


# create an instance of chrome browser 
driver = webdriver.Chrome()

# Go to the page you want to the scrape the data 
driver.get("https://app.daily.dev/popular")

# Get the html of the page and parse it to beautiful soup

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

posts = soup.find("a", class_="focus-outline absolute inset-0 block h-full w-full rounded-16")

print(soup)

driver.quit()