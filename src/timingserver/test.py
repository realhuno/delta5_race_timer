# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "http://192.168.42.1/api/v1/lap_track"
 
# your API key here
transponder= "1"
 
data = {'transponder_token':transponder,
        'lap_time_in_ms':'15000'}
 
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)
 
# extracting response text 
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)
