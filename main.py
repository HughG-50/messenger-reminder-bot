import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
browser = webdriver.Chrome(options=options)

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

browser.get("https://www.messenger.com/login")
print(f"Navigated to {browser.title}")

time.sleep(5)
email_input = browser.find_element(By.ID, "email")
password_input = browser.find_element(By.ID, "pass")
login_button = browser.find_element(By.ID, "loginbutton")

email_input.send_keys(username)
time.sleep(3)
print(email_input.get_attribute("id"))
print(email_input.get_attribute("value"))

password_input.send_keys(password)
time.sleep(4)
print(password_input.get_attribute("id"))
print(bool(password_input.get_attribute("value")))

login_button.click()
time.sleep(11)

chat_list_container = browser.find_element(By.CSS_SELECTOR, "[aria-label=Chats]")
chat_first_element = chat_list_container.find_element(By.CSS_SELECTOR, "div[data-testid='mwthreadlist-item-open']")
chat_first_element.click()
time.sleep(3)

chat_input = browser.find_element(By.XPATH, "//div[@role = 'textbox']")
chat_input.send_keys("Post your screentime screenshots")
time.sleep(5)
submit_button = browser.find_element(By.XPATH, "//div[@aria-label='Press Enter to send']")

submit_button.click()
time.sleep(10)

browser.quit()