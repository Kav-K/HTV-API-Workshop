import requests
#This import is actually used now, we use this to convert our input dictionary to JSON to use as a part of the request
import json

#The header Content-Type : application/json tells the endpoint that it will receive data in JSON format! This request will
#NOT work without this! Try it out yourself by removing it.
request_headers = {"Content-Type": "application/json"}

#The JSON object (python dictionary) to send to the API
input = "Hello world"
data_to_send = {"INPUT": input}

#The endpoint for the API
api_url = "http://api.shoutcloud.io/V1/SHOUT"

#We make the actual request here, this seems similar to the last program, right? The difference here is that we
# use the post() method instead and also send it the headers!
response = requests.post(url=api_url, data=json.dumps(data_to_send), headers=request_headers)

#Read the response as JSON and print out the "OUTPUT" field!
print(response.json()['OUTPUT'])
