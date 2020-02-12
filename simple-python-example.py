import requests
import json

#Make the actual request to the API using the python requests library
#You may need to run the command 'pip install requests' in your terminal
api_request_response = requests.get(url="https://api.ratesapi.io/api/latest?base=CAD")

#Convert the data into a JSON object in python
response_data = api_request_response.json()
print(response_data)

#Programatically, you can manipulate JSON data just like a python dictionary
#If you are not familiar, python dictionaries use key:value pairs to store data
dictionary_example = {"myKey":"myValue"}
print(dictionary_example["myKey"])

#Using this one our data, we can get specific values out of the large JSON data set that we got as
#a response. For example, to print the base currency we can do:
print("The base currency is: " + response_data["base"])

#To print the conversion rate with GBP, we can do:
print("The conversion rate for CAD and GBP is: "+ str(response_data["rates"]["GBP"]))
#Keep in mind that you might have to cast values to different data types to make it work with your program!


#Lets ramp it up a bit, lets print all of the conversion rates with a loop
for key,value in response_data["rates"].items():
    print("The conversion rate for "+key+" is "+str(value))

#ALternatively:
for key in response_data["rates"]:
    print("THe conversion rate for "+key+" is "+str(response_data["rates"][key]))
    
