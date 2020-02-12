# Part 2
This section will aim to give you an understanding of how to programatically make API requests and use the data

# Some notes before starting
You're going to want to clone this repository, and switch to this branch (part-2) if you want the python files to follow along! Or you can download the file directly from the web version of github by just clicking on it and clicking download!
You will most likely also need to type 'pip install requests' in your command line for the code to work, as it uses a library called requests to fulfil our HTTP requests to the APIs!

# A simple Python to make HTTP GET requests
The program simple-python-request-get.py is a very simple example of how to use python to programatically make HTTP GET requests and to use the data that is returned from it! It uses a library called "requests" to make a GET request to any URL that you specify, then it saves the output in a variable called `api_request_response`, we then convert it into JSON and save it in a variable called `response_data`. 

JSON and Python are friendly, in fact, they're so friendly that you can treat a JSON object in python as a simple dictionary! This makes sense, because a python dictionary is a store of key:value pairs, and so is JSON.

If you need a refresher, a python dictionary looks like (and is defined as) this:

```
fruit_colors = {
  "apple": "red",
  "orange": "orange",
  "banana": "yellow"
}
```
This looks familiar, right? Yes! It does, because it is identical to how a JSON object looks! In fact, it is syntactically the same as the response that we got when making a request to the Rates API earlier in this workshop!

The equivalent JSON object for fruit_colors would look like this:

```
   "fruit_colors": {
   "apple":"red",
   "orange":"orange",
   "banana":"yellow"
}
```

In python, to obtain a value from our fruit_colors dictionary, we would do something like `fruit_colors[key]` with the *key* being the value of the key in the pair we want to find the value for (Yeah, thats a mouthful). For example:

`banana_color = fruit_colors['banana']`

This would return us the value for the key 'banana' in our dictionary fruit_colors!

Now, lets go back to the reponse that we got from earlier when we made a request to the Rates API:

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

What would the python dictionary equivalent of this big JSON object look like? Hint: it would look *very* similar:

```

rates_dictionary = {
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
What did we do? We *literally* just added `rates_dictionary =` to the beginning of that JSON block, as you can see, JSON and python dictionaries are considered identical.

Now that we can think of JSON objects as python dictionaries, we know that we can access individual pieces of data just like we did with the fruit_colors dictionary. For example, if we wanted to access the base currency, we would do something like

`base_currency = rates_dictionary['base']`

If we wanted to access the exchange rate of BGN, we would do something like

`bgn_rate = rates_dictionary['rates']['BGN']`

The block `rates_dictionary['rates']` is what we call a *multilevel dictionary*.

Now that you have been refreshed on python dictionaries and its relationship with JSON, feel free to try out the program and see how it works! It's a short and concise program


<a href="https://github.com/Kav-K/HTV-API-Workshop/tree/part-3"><h3>Click here to go to Part 3 (or switch your branch to part-2)</h3></a>
