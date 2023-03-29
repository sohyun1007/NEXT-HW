import re
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains

# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = '/Users/sohyunlim/Desktop/NEXT-HW/Session5/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20230328" 
driver.get(url)
time.sleep(1)

search_text = "소울"
search_box = driver.find_element(By.XPATH,'//*[@id="ipt_tx_srch"]')
search_box.send_keys(search_text)
search_box.send_keys(Keys.RETURN)

time.sleep(2) 
movie_link = driver.find_element(By.XPATH,'//*[@id="old_content"]/ul[2]/li[1]/dl/dt/a')
movie_link.click()

time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

with open('favorite_movie.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    
    title = soup.find("h3", class_="h_movie").find("a").text.strip()
    director=driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
    rating_review_count=driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[3]/strong/em').text
    
    writer.writerow([title, director, rating_review_count])