# Part 3
This section will show you how to get set up with Google Cloud!

# Creating your account
You can create your account with the link on the GCP Promotion Cards that you might have gotten or found at the event, but if you haven't received one, you will still get $300 for free! You can register through <a href="https://cloud.google.com/free">THIS LINK</a>. If you want to learn more about what the 'GCP Free Tier' entails, you can click on <a href="https://cloud.google.com/free/docs/gcp-free-tier">this other link</a>. You will be asked to enter your credit/debit card details but Google will <b>NOT</b> ever charge you unless you explicitly ask them to, they will not even charge you after your free trial credits run out, or when your trial ends so you have nothing to worry about!

# Exploring and enabling the Places API
Great! Now that you've signed up and set up your free trial, we can actually start exploring what the Google Cloud Platform has to offer.
At the very basic, home page of GCP, you will see something like this:
<img src="https://i.imgur.com/xoZBqRh.png"/>
On the left, the scrollbar menu shows you all the different offerings that GCP has, and the right side shows you the dashboard view with all the useful widgets that you may need. It may look overwhelming at first but you get used to it!

Before we get further into it, you might be asking, why are we using the Places API? A Google Maps API? What about the cool and fancy machine learning stuff? The answer to that is this; it is better to get a basal understanding of something rather than dive into something fancy and not understand what it derives from and what the fundamentals are. Too often I see hackathon attendees using GCP,Azure, or AWS APIs simply by copying and pasting code from stackoverflow, without an actual understanding of what they are doing. Those projects usually do not end well because of severe lacks of understanding! The Places API provides us with a simple and intuitive, but also very powerful starting point.

Now, lets get started and find this Places API! In the search bar at the top, type "Places API":
<img src="https://i.imgur.com/AXhryPw.png"/>
You will then see a screen that looks like this, you will then want to click the Enable button to get started and to let GCP know that you will be using this API:
<img src="https://i.imgur.com/vWAU4DQ.png"/>
Once enabled, we have another step to do before we can start actually using it. Google Cloud Platform requires authentication in order for you to use their APIs, this is to prevent just anybody from using the APIs! We will need a credential in order to access this API in the form of an "API Key", we can make one for ourselves by clicking in the credentials tab:
<img src="https://i.imgur.com/h1Jw569.png"/>
Then, we will click on the hyperlink that leads us to the create a new credential page:
<img src="https://i.imgur.com/UrR4tJf.png"/>
Then, we will click "Create Credentials" near the top of that page:
<img src="https://i.imgur.com/TVb70YM.png"/>
Click the popup that says "API key"
<img src="https://i.imgur.com/IZJvLec.png"/>
After that, you should receive a pop up that says your API key was successfully created, and then you should copy this key into your clipboard because we will be using it very shortly!

As you probably saw on that page, there are other options for creating credentials too, such as OAuth Tokens and Service Accounts! These are useful and give you more flexibility, but we don't need any of them for our purposes right now.

Now, lets start actually using the Places API! The first thing you do before using ANY API is read the documentation! In our case, the documentation for the Places API can be found at https://developers.google.com/places/web-service/search 

# Our Program
Our goal is to make a very simple python program where a user can input some sort of search query (for example, "Pizza Hut in Scarborough") and our program will return a list of all of the places that match that query with details about them!

NOTE: The actual program will be covered and explained and written together with the physical workshop participants, so come on out! The rest of this document however will give you enough information to help you try and do it yourself based on the previous programs that we've made!

# Making a request to the API
So, remember that API key we made earlier? Lets use it! 
The documentation for the Places API gave us some useful information, specifically, it gave us the endpoint that we should request to if we wanted to do a "text search", that endpoint is 

`https://maps.googleapis.com/maps/api/place/textsearch/output?parameters`

It also gave us some further information about how to use the API, more specifically, it said that we should replace `output` with whatever output type we want, in our case, we will replace it with `json`. Next, it gave us a set of parameters that we can use! Lets have a look at them:

<img src="https://i.imgur.com/3SS5snS.png"/>

This is useful! This gives us absolutely everything we need to get started with the API.
The parameters that we are especially interested in are `key` and `query`. The value for `key` will obviously be our API key, and the value for `query` will be the text that we would like to search! Our request URL should look something like this:

`https://maps.googleapis.com/maps/api/place/textsearch/json?key=asujdu1euaYOUR_KEY_HERE&query=Pizza Hut in Scarborough`

Now, before we start programatically interacting with it, type that link into your web browser, what do we get?:
```
{
   "html_attributions" : [],
   "results" : [
      {
         "formatted_address" : "592 Ellesmere Rd, Scarborough, ON M1R 4E9, Canada",
         "geometry" : {
            "location" : {
               "lat" : 43.763754,
               "lng" : -79.2921058
            },
            "viewport" : {
               "northeast" : {
                  "lat" : 43.76484802989273,
                  "lng" : -79.29078412010729
               },
               "southwest" : {
                  "lat" : 43.76214837010728,
                  "lng" : -79.29348377989272
               }
            }
         },
         "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/restaurant-71.png",
         "id" : "343f662a9696f8c256cd8578840f61bf0fa7bbcf",
         "name" : "Pizza Hut",
         "opening_hours" : {
            "open_now" : true
         },
         "photos" : [
            {
               "height" : 3024,
               "html_attributions" : [
                  "\u003ca href=\"https://maps.google.com/maps/contrib/113250507798331324263\"\u003eShaarujon Vijayakumar\u003c/a\u003e"
               ],
               "photo_reference" : "CmRaAAAAzfHdZBqdj0M8W3iiUa24pmYxvk78W90z8yYiYYs05HXWrZaZ_mJcaOYMVKXdwencmOKqKhn92avGxe3Iwn9G4TXaDj6dIXtmGWb-ugjCyobihbKY78olX6VEuMvVzPO6EhDQxUwp-WS519ilU4dgIEBsGhR6bl0SblD5ga8z3clhDErZ424ocQ",
               "width" : 4032
            }
         ],
```

Familiar, right? That's a nice, clean, JSON response like earlier! Now that we know about JSON we are also ready to start using it programatically!

The program for making queries with python will be written and demonstrated during the physical workshop! If you aren't feeling up to coming, or you are in the workshop right now and you're bored, feel free to download the program parse.py from this branch! (It is the final product)


</a>
