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

with open('movie_info.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    for i in range(2,23):
      try:
          title_temp = driver.find_element(By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[{i}]/td[2]/div/a')
          title=title_temp.text
          print(title)
          title_temp.click()
          time.sleep(0.1)
  
          director_temp=driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
          print(director_temp)
         
          outline_temp=driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[1]/div/div/p').text

          rating_temp = driver.find_element(By.XPATH, '//*[@id="actualPointPersentBasic"]/div/span/span').text
          
          rating_lst= re.findall(r'\d+\.\d+', rating_temp)
          
          rating = rating_lst[0] if rating_lst else None
          print(rating)
          
          writer.writerow([title, director_temp, outline_temp, rating])

          driver.get(url)
          time.sleep(0.1)
      except:
          print('존재하지 않는 영화입니다.')
          driver.get(url)
          time.sleep(0.1)

