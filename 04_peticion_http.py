# Este program hace una petcion a HTTP

import requests

response = requests.get('https://galileoguzman.com/')
print(response.text)