import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import urllib.parse

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

try:
    element = WebDriverWait(driver, 1200).until(
        EC.presence_of_element_located((By.CLASS_NAME, "iq0m558w")) # wait for the page to load
    )
except Exception as e:
    print(e)

def read(rkve):
    openkve = open(rkve, 'r')
    return csv.reader(openkve, delimiter=',')

def send(l):
    name=l[0]
    number=l[1]
    message=l[2]
    nameIn = f"{name}, {message}"
    text = urllib.parse.quote_plus(nameIn)
    link = f"https://web.whatsapp.com/send?phone={number}&text={text}"
    driver.get(link)
    try:
        element = WebDriverWait(driver, 1200).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_3Uu1_"))
        )
    except Exception as e:
        print(e)
    sleep(1)
    actions=ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    sleep(10) #slow internet
    
    print("complete")

data = read('../contact.csv')
for j in data:
    send(j)

driver.quit()
