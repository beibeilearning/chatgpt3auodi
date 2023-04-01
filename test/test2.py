import requests
from bs4 import BeautifulSoup

# 构造要爬取的页面 URL
stock_code = 'sz000002'
url = f'http://quote.eastmoney.com/{stock_code}.html'

# 发送 HTTP 请求，获取页面内容
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

# 解析页面内容，提取股价信息
soup = BeautifulSoup(html, 'html.parser')
price_tag = soup.select_one('.last')
price = price_tag.get_text()
print(f'{stock_code} 当前股价：{price}')