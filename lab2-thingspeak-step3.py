import http.client
import urllib.parse
import requests
import time
key = "69WA488NQ3J1CG6P"  # Put your API Key here
def read_data_thingspeak():
    URL = 'https://api.thingspeak.com/channels/1156612/fields/1.json?api_key='
    KEY = '2Z8UW2HQ24RONT0Z'
    HEADER = '&results=2'
    NEW_URL = URL+KEY+HEADER
    
    get_data = requests.get(NEW_URL).json()
    print(get_data)
    channel_id = get_data['channel']['id']
    
    field_1 = get_data['feeds']
    print(field_1)
    t = []
    for x in field_1:
        
        t.append(x['field1'])
    print(t)
        
if __name__ == '__main__':
     read_data_thingspeak()   