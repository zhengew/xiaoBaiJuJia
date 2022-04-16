import requests

ret = requests.get('http://8.129.162.225/login?redirect=%2Findex')
print(ret.text)