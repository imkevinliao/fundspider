import requests
import os
from FackUA import my_fake_ua


header = {"User-Agent": my_fake_ua.random}
url = r'https://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?&page=1'
res = requests.get(url, headers = header)
content = res.text

with open('result.txt', 'w', encoding = 'utf-8') as f:
    f.write(content)


