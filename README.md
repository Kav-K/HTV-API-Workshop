# Part 1
This section will aim to give you an understanding of what APIs are and why we use them.

# What is an API?
An API is a means for a company, organization, or individual to make their data or functions/features accessible and integratable for a large amount of developers without the need for the developer themself to put in a large amount of overhead work. For an example, the <a href="https://openweathermap.org/api">OpenWeatherMap API</a> provides developers with a way to access on-demand and reliable weather data for locations all across the world without the developer needing to do any work in the collection of that data. They simply make a quick request to the API and they will get data back instantly. Another example is the <a href="https://api.ratesapi.io/api/latest">Rates API</a> which is a free API that displays accurate and real-time exchange rates for foreign and domestic currency.

# What can you use APIs for?
I think the answer to this question should be pretty clear by now hopefully! You can use APIs to access data from companies, organizations, or individuals, (e.g: going back to the OpenWeatherMap API, you can use it in your application to get weather data on demand for your users) and you can use APIs to access certain functions from different providers as well. That all sounds good, but how do we start using APIs?

# How do you use an API?
The primary method of communication for *most* APIs is through HTTP requests. You would simply make an HTTP (GET,POST,CREATE,UPDATE,etc) request to an endpoint. The most common types of HTTP requests are GET and POST. An endpoint is an external facing service that is open to the internet, or your internal network that accepts requests to the API, processes them, and then returns back a response! An endpoint could be an IP address (e.g 192.180.0.1) or an endpoint could be a web link (http://mywebsite.com/api). Most API endpoints are web links like the latter. We will not get into the details of how they work and how to write them, because that's out of the scope of this workshop, instead we will focus on how to use them, such as how to make requests to them and do stuff with the data that we get back!

# Making a request to an API
In this very simple demonstration, we will make a GET request to the Rates API, the Rates API is an API that displays and returns back the current exchange rates for foreign currency. To make a request to this API all you have to do is send it an HTTP request! You can very simply make an HTTP GET request using a browser by just putting the link to the API in the address bar of your browser. Try it out! Copy this link and paste it into your address bar in another tab: `https://api.ratesapi.io/api/latest`

You should see a bunch of seemingly messy information that looks something like this:

`{"base":"EUR","rates":{"GBP":0.84325,"HKD":8.4658,"IDR":14919.11,"ILS":3.72,"DKK":7.4721,"INR":77.6945,"CHF":1.0667,"MXN":20.3563,"CZK":24.965,"SGD":1.5127,"THB":34.082,"HRK":7.459,"MYR":4.5059,"NOK":10.0953,"CNY":7.6025,"BGN":1.9558,"PHP":55.061,"SEK":10.5373,"PLN":4.2569,"ZAR":16.2331,"CAD":1.4495,"ISK":137.9,"BRL":4.6995,"RON":4.7693,"NZD":1.7055,"TRY":6.5775,"JPY":119.73,"RUB":69.3198,"KRW":1290.63,"USD":1.0901,"HUF":337.93,"AUD":1.626},"date":"2020-02-11"}`

# What is this stuff? How can we use it?
The response that you got (the html you saw in the browser after putting the link in the address bar) is in a format called JSON. the JSON format is a data format that a very large majority of APIs will use, because it is supported well and it is simple to interpret and use programatically. If we clean it up a little bit with a tool called <a href="https://jsonlint.com/">JSON Lint</a> we can see that the data itself is actually quite neatly arranged:

```
{
	"base": "EUR",
	"rates": {
		"GBP": 0.84325,
		"HKD": 8.4658,
		"IDR": 14919.11,
		"ILS": 3.72,
		"DKK": 7.4721,
		"INR": 77.6945,
		"CHF": 1.0667,
		"MXN": 20.3563,
		"CZK": 24.965,
		"SGD": 1.5127,
		"THB": 34.082,
		"HRK": 7.459,
		"MYR": 4.5059,
		"NOK": 10.0953,
		"CNY": 7.6025,
		"BGN": 1.9558,
		"PHP": 55.061,
		"SEK": 10.5373,
		"PLN": 4.2569,
		"ZAR": 16.2331,
		"CAD": 1.4495,
		"ISK": 137.9,
		"BRL": 4.6995,
		"RON": 4.7693,
		"NZD": 1.7055,
		"TRY": 6.5775,
		"JPY": 119.73,
		"RUB": 69.3198,
		"KRW": 1290.63,
		"USD": 1.0901,
		"HUF": 337.93,
		"AUD": 1.626
	},
	"date": "2020-02-11"
}
```

Clean, right?
JSON stores data in key-value pairs, similar to that of a Dictionary in python, or a HashMap in java, if you've used them before. In the data that we got, we can see that in `"base": "EUR",` the key is *base* and the value is *EUR*. If you look one line after that, the key is *rates* and the value is another JSON object that consists of all of the exchange rates! If you're familiar with Python, you can think of it as a bunch of nested dictionaries! Or you can think of it as mappings within mappings, with no real limits.

Now, we see that the base currency is EUR, but we're not in Europe! (unfortunately) How do we change that? Luckily for us, the API developer has written a feature that lets us change that by sending a request with a *parameter* to the API!

# Parameters
A lot of the times, APIs will have things called parameters, what parameters do is they allow you to request different things from the API. In our case, we want to request that the base currency be "CAD" instead of "EUR". We will do this by modifying a parameter in the request to the API called "base". Like JSON, parameters are also with the request to the API in key=value pairs. They look like this for a GET request:

`http://mywebsite.com/api?a_parameter=a_value`

The `?` denotes the start of a list of parameters! 
What if you wanted to have multiple parameters? It would look like this:

`http://mywebsite.com/api?a_parameter=a_value&another_parameter=another_value`

Simple? right?

Let's try it with the rates API. The parameter is called "base" and the value is called "CAD", so our GET request would look like this:

`https://api.ratesapi.io/api/latest?base=CAD`

After you type that into your browser, you should see a similar response to earlier, but with the base currency now being CAD!

# GET and POST requests
In this example, we did a HTTP GET request, without diving too much into the details, the different between the two is as follows; a GET request is used to obtain/retrieve information from a resource or API, and a POST request is used to send data to a a resource or api! We would use a GET request when we simply want to make a request with a few parameters, and we would use a POST request when the API requires us to submit some piece of data before it can give us a response. Another thing to keep in mind is that parameters are sent in the URL of the API for a get request, like above:

`https://api.ratesapi.io/api/latest?base=USD`

However, with a POST request, the parameters for the request are sent in what's called the *body* of the request, the request ends up looking something like this:

```POST /path/to/my/api HTTP/1.0
User-Agent: HTTPTool/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 32

a_parameter=a_value&another_parameter=another_value
```

You've now learned how to make a request to an API and how they work in a generalized sense, continue to the next part where we start programatically using the data!

<a href="https://github.com/Kav-K/HTV-API-Workshop/tree/part-2"><h3>Click here to go to Part 2 (or switch your branch to part-2)</h3></a>
