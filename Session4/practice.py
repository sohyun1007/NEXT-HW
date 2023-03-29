from bs4 import BeautifulSoup
import requests as req
import pandas as pd

target_url = "https://opentutorials.org/course/1"

res = req.get(target_url)
# BeautifulSoup(첫번째 인자, 두번째 인자) - 첫번째 인자를 두번째 인자로 읽어라(res.text를 html로 읽어라)
soup = BeautifulSoup(res.text, "html.parser")

print(res)
# res결과값 <Response [200]>

print(res.text)
# 구체적인 결과값을 알고 싶다면 res.text로 안에 있는 내용 파악

print(soup)
# soup의 결과값을 보면 rest.text의 결과값과 별 차이가 없다고 생각할 수도 있는데

#print(res.text.li)
# 이렇게 res.text에서 <li>를 출력하고 싶어서 res.text.li를 해보면 안돼!
# 왜 안돼? 파이썬은 몰라 res.text가 html인지 그래서 res.text에서 <li>를 봐도 그게 태그인지 알지 못하는거지

print(soup.li)
# 하지만 BeautifulSoup로 이 아이는 html이야! 라고 알려준 후에는 soup.li하면 <li>태그를 잘 찾지!
# 이렇게 --- 이게 html인지 text인지 모르느 파이썬에게 이건 html이야! --- 라고 친절하게 알려주는게 BeautifulSoup

# find_all(조건)은 조건에 맞는(원하는 것)을 모두 가지고 오는거야!
# 예를 들어, soup.find_all("li")하면 <li>태그 모두를
print(soup.find_all("li"))

# 그러면 find_all(클래스가 ""인 것!)이렇게 조건을 달고 싶다!
# find_all(class="")하면 좋겠지만, 파이썬에는 class가 있잖아 그래서
# find_all(class_="")이렇게 클래스가 ""인 것을 찾는대
print(soup.find_all(class_="comment_content"))

# 위처럼 태그들에 둘러싸여서 너무 보기 어렵다 할 때
content = soup.find_all(class_="comment_content")
content_cleaned = [e.text.strip() for e in content]
print(content_cleaned)

print(soup.select('div.name.time > strong'))

print(soup.select('div.name.time > a'))