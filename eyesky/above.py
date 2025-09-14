# https://www.n2yo.com/api/#above
# Request: /above/{observer_lat}/{observer_lng}/{observer_alt}/{search_radius}/{category_id}

import requests
import json

lat = 53.21667
long = -1.01667
elevation = 47
key = 'API_KEY'

def above(lat, long, elevation):
    url = f'https://api.n2yo.com/rest/v1/satellite/above/{lat}/{long}/{elevation}/5/0&apiKey={key}'
    response = requests.get(url)
    data = response.json()
    return data

print(json.dumps(above(lat, long, elevation), indent=4))
