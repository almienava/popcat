from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import sys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--mute-audio')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

app = '//*[@id="app"]'
url_= "https://popcat.click/"
driver.get(url_)
cat = driver.find_element('xpath',app)
sys.stdout.reconfigure(line_buffering=True)
count = 0
print("Bot PopCat Di Mulai")
while True:
    cat.click()
    count+=1
    print(f"click yang ke {count}")