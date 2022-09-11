import requests
import pprint
session = requests.Session()
res = session.get('http://httpbin.org/get')
pprint.pprint(res.status_code)