import requests
url = 'http://m.ip138.com/ip.asp?ip='
print('请输入您要查询的IP地址')
ip_add = input()
try:
    r = requests.get(url+ip_add)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('爬取失败')