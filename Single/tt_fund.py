import ast
import json

import requests
from fake_useragent import UserAgent


def get_content():
    url = r'https://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?&page=1'
    header = {'User-Agent': UserAgent().random}
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url, headers=header, verify=False).text
    return res


if __name__ == '__main__':
    content = get_content()
    if content:
        ...
