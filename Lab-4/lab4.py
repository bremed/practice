import http.client
import urllib.parse
import time

key = "7481QW0APO2BO2BU"  # Put your API Key here
group = "L1-F-1"
member = "b"
email = "brettmedjuck@cmail.carleton.ca"
params = urllib.parse.urlencode({'field1': group, 'field2': member,'field3': email,'key':key })
headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = http.client.HTTPConnection("api.thingspeak.com:80")
try:
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print(group)
    print(member)
    print(email)
    print(response.status, response.reason)
    data = response.read()
    conn.close()
except:
    print("connection failed")