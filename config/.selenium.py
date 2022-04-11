import os
import re
import math
import sys
import json
import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

def main():

  # Run in headless mode

  options = webdriver.ChromeOptions()
  options.add_argument("--headless")
  options.headless = True

  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(options=options, service=service)
  driver.maximize_window()

  page = sys.argv[1]

  #pages_api = os.getenv("PAGES_URL")
  #data = json.loads(pages_api)
  #endpoint = data["html_url"]

  # Local Testing
  driver.get(f"https://chat.cmpsc302.chompe.rs/{page}")
  #driver.get(f"{endpoint}{page}")

  username_entry = driver.find_element(by=By.CSS_SELECTOR, value="#nameEntry")
  username_submit = driver.find_element(by=By.CSS_SELECTOR, value="#setName")

  username_entry.send_keys("Ulysses")
  username_submit.click()

  chat_entry = driver.find_element(by=By.CSS_SELECTOR, value="#sendMsg")
  chat_submit = driver.find_element(by=By.CSS_SELECTOR, value="#sendBtn")

  for _ in range(20):
    chat_entry.send_keys("Meow")
    chat_submit.click()
    sleep(12)

  chat_messages = driver.find_elements(by=By.CSS_SELECTOR, value=".chat-msg")

  if len(chat_messages) > 20:
    exit(0)
  exit(1)

if __name__ == "__main__":
  main()
