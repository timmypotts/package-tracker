import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get("SHIPENGINE_API_KEY")

def track(tracking, carrier):
    carrier = carrier.lower()

    url = "https://api.shipengine.com/v1/tracking?carrier_code=" + carrier + "&tracking_number=" + tracking

    payload = {}
    headers = {
    'Host': 'api.shipengine.com',
    'API-Key': key
    }

    response = requests.request("GET", url, headers=headers, data = payload)


    res = response.text.encode('utf8')
    json_obj = json.loads(res)
    print(json_obj)
    return json_obj