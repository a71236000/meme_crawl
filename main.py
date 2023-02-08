from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from PIL import Image
from selenium.webdriver.chrome.options import Options
import urllib.request
import time
import requests


def crawl_from_ig():
    wd = webdriver.Chrome(service=Service('C:\chromedriver.exe'))
    wd.implicitly_wait(8)
    wd.maximize_window()

    time.sleep(1)

    wd.get("https://www.instagram.com")

    time.sleep(1)



    wd.find_element(By.NAME, "username").send_keys("testcrawl1234")
    wd.find_element(By.NAME,"password").send_keys("bb617091")

    wd.find_element(By.XPATH,"//*[text()='登入']").click()
    wd.find_element(By.XPATH,"//*[text()='稍後再說']").click()
    wd.find_element(By.XPATH, "//*[text()='稍後再說']").click()
    time.sleep(1)
    wd.get("https://www.instagram.com/godreplyme")
    scroll_time = int(input('請輸入想要捲動幾次'))

    for now_time in range(1, scroll_time + 1):
        time.sleep(1)
        print(f"now scroll {now_time}/{scroll_time}")
        js = "window.scrollTo(0, document.body.scrollHeight);"
        wd.execute_script(js)
    print('scroll_finish')
    time.sleep(2)
    # 定位到 Class name "_aagw" 下面的所有圖片
    images = wd.find_elements(By.XPATH,"//div[@class='_aagv']/img")
    print(images)
    # 遍歷所有圖片，下載並保存為 JPG 檔
    for i, image in enumerate(images):
        src = image.get_attribute("src")
        response = requests.get(src)
        with open(f"{i}.jpg", "wb") as f:
            f.write(response.content)



crawl_from_ig()