from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import  time



url = 'http://adamchoi.co.uk/teamgoals/detailed'
service = Service(executable_path='./chromedriver.exe')  # Path to the chromedriver.exe.
"""
- service is an instance of the Service class. It is used to start the ChromeDriver server.
"""

driver = webdriver.Chrome(service=service) # The driver is an instance of the Chrome class.
print('Opening the browser...')
driver.get(url)

# selecting the button with xpath
button = driver.find_element(By.XPATH, "//label[@analytics-event = 'All matches']")
button.click()

# Wait for 5 seconds
time.sleep(5)
print('Closing the browser...')
driver.quit()
