# 20web.py 

import requests
from bs4  import BeautifulSoup
import re

# https://ko.wikipedia.org/wiki/인공지능
url = "https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0 (compatible; MyRAGBot/1.0; +https://example.com/bot)"}
)

soup = BeautifulSoup(response.text, "html.parser")
# 전체 텍스트 가져오기
raw_text = soup.get_text()
print(raw_text)
print('web크롤링 연습 12:59 1:09')

# # 공백 정리
clean_text = re.sub(r"\s+", " ", raw_text).strip()
# print(clean_text)
# print()

print('- ' * 50)
summary = clean_text[:1000]
print(summary)
