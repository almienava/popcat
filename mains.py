from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import sys
from threading import Thread

def init_chromeDriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument('--mute-audio')
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

def click_process(num_thread):
    driver = init_chromeDriver()
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
        print(f"[thread[{num_thread}]]total clicked {count}")

if __name__ == "__main__":
    total_thread = int(input('input total thread : ')
    for x in range(total_thread):
        t = Thread(target=click_process,args=(x,))
        t.start()
