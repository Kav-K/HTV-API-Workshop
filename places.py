import requests
import json

SEARCH_ENDPOINT = "https://maps.googleapis.com/maps/api/place/textsearch/json"
DETAILS_ENDPOINT = "https://maps.googleapis.com/maps/api/place/details/json"
API_KEY = "AIzaSyBNptDO4MXjTv7C-yEaKi1nBCnN1uZPcbU"
#This is just some safe default headers to make sure our connection doesnt somehow get dropped! Ignore these for now
headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}

#The API to get details about a place given a place id!
def api_details(id):
    parameters = {"place_id":id, "key":API_KEY}

    response = requests.get(url=DETAILS_ENDPOINT,params=parameters, headers=headers)

    return response.json()

#The API to search for a place given some query text
def api_search(text):
    parameters = {"query": text, "key":API_KEY}

    response = requests.get(url=SEARCH_ENDPOINT,params=parameters, headers=headers)

    return response.json()

#Main program loop
while True:
    try:
        input_text = input("Enter your query text: ")
        if (input_text == "quit"): exit(0)

        for result in api_search(input_text)['results']:
            print("")
            print("Name: " +result['name'])
            print("Address: "+result['formatted_address'])

            details = api_details(result['place_id'])
            print("Hours: ")

            if 'result' not in details: continue

            #These if statements check if the key is actually in the JSON object, AKA they check if the place actually
            # has opening hours, or has reviews before trying to access them! This is a safe practice
            if 'opening_hours' in details['result'] and 'weekday_text' in details['result']['opening_hours']:
                for open_day in details['result']['opening_hours']['weekday_text']:
                    print("  "+open_day)
            if 'reviews' in details['result']:
                print("Most Recent Review: ")
                print("   Rating: "+ str(details['result']['reviews'][0]['rating']))
                print("   Text: " + details['result']['reviews'][0]['text'])
    #Exit on ctrl+c
    except KeyboardInterrupt:
        print("Exiting program")
        exit(0)


