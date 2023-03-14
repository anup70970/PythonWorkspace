

import requests 
import json

consul_host = "http://localhost:8500"

# Fetch a key value from consul
def fetch_key_value(key):
    response = requests.get(consul_host + "/v1/kv/" + key)
    if response.status_code == 200:
        return json.loads(response.text)[0]["Value"]
    else:
        return None

# Example Usage
value = fetch_key_value("my_key")
if value:
    print(value)
else:
    print("Key not found")