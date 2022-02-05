import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)

browser.get("https://www.google.com")
print(browser.title)

# ###############
# REMOVE COMMENTS ONCE WORKING ON HEROKU
# ###############

# username = os.getenv('USERNAME')
# password = os.getenv('PASSWORD')

# browser.get("https://www.messenger.com/login")
# print(f"Navigated to {browser.title}")

# time.sleep(5)
# email_input = browser.find_element(By.ID, "email")
# password_input = browser.find_element(By.ID, "pass")
# login_button = browser.find_element(By.ID, "loginbutton")

# email_input.send_keys(username)
# time.sleep(3)
# print(email_input.get_attribute("id"))
# print(email_input.get_attribute("value"))

# password_input.send_keys(password)
# time.sleep(4)
# print(password_input.get_attribute("id"))
# print(bool(password_input.get_attribute("value")))

# login_button.click()
# time.sleep(11)

# chat_list_container = browser.find_element(By.CSS_SELECTOR, "[aria-label=Chats]")
# chat_first_element = chat_list_container.find_element(By.CSS_SELECTOR, "div[data-testid='mwthreadlist-item-open']")
# chat_first_element.click()
# time.sleep(3)

# chat_input = browser.find_element(By.XPATH, "//div[@role = 'textbox']")
# chat_input.send_keys("📱📱 Post your screentime screenshots 🧐 🧐 ")
# time.sleep(5)
# submit_button = browser.find_element(By.XPATH, "//div[@aria-label='Press Enter to send']")

# submit_button.click()
# time.sleep(10)

# browser.quit()