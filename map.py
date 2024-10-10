import requests


def get_lat_long(address):

    
    api_key = "MAP-API"
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    if data["status"] == "OK":
        lat = data["results"][0]["geometry"]["location"]["lat"]
        lng = data["results"][0]["geometry"]["location"]["lng"]
        whole_add = ""
        for i in data['results'][0]['address_components']:
            whole_add += f"{i["long_name"]} "
        return lat, lng,whole_add
    else:
        return None, None, None
    
