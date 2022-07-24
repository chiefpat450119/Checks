import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.sg/gp/product/B08HNSWWT7?&linkCode=sl1&tag=geekcult-22&linkId=1793faf85e4cb04784c682cdec4ed987&language=en_SG&ref_=as_li_ss_tl'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

availability = soup.find(id='availability').get_text()
messages = availability.split('.', 1)
for message in messages:
    print(message.strip())

input('Press ENTER to exit')