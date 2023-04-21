import requests
import random
import string
# 소문자 문자열
letters = string.ascii_lowercase
for article_pk in range(1, 20):
    url = f'http://127.0.0.1:8000/api/v1/articles/{article_pk}/comments/'
    for _ in range(5):
        # 소문자 아무거나 10개 뽑아서 반환 - 제목, 내용
        # title = ''.join(random.choice(letters) for _ in range(10))
        content = ''.join(random.choice(letters) for _ in range(10))
        response = requests.post(
            url, data={'content': content})
