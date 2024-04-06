# 2+2
import requests


url = f"{input()}:{input()}?a={input()}&b={input()}"
response = requests.get(url).json()
print(*sorted(response['result']))
print(response['check'])
