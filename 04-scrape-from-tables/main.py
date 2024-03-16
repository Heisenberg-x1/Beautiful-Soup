from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set the path to the chromedriver executable
path = "../03-selenium/chromedriver.exe"

# url of the page
url = 'http://adamchoi.co.uk/teamgoals/detailed'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=Service(path))

print('Opening the browser...')
driver.get(url)
button = driver.find_element(By.XPATH, "//label[@analytics-event = 'All matches']")
button.click()
matches = driver.find_elements(By.TAG_NAME, 'tr')

dates = []
home_teams = []
scores = []
away_teams = []

for match in matches:
    # date = match.find_element(By.XPATH, 'td[1]').text
    # home_team = match.find_element(By.XPATH, 'td[2]').text
    # score = match.find_element(By.XPATH, 'td[3]').text
    # away_team = match.find_element(By.XPATH, 'td[4]').text
    dates.append(match.find_element(By.XPATH, 'td[1]').text)
    home_teams.append(match.find_element(By.XPATH, 'td[2]').text)
    scores.append(match.find_element(By.XPATH, 'td[3]').text)
    away_teams.append(match.find_element(By.XPATH, 'td[4]').text)

df = pd.DataFrame({'Date': dates, 'Home Team': home_teams, 'Score': scores, 'Away Team': away_teams})
df.to_csv('matches.csv', index=False)
print('Closing the browser...')
driver.quit()  # Close the browser
