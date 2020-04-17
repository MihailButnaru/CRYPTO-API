<div align="center">
<h1> Crypto Analysis RESTful API </h1>
<p1>The Crypto API is designed to be a predictable and intuitive interface for
interactive with analysed data from Twitter.</p1>
</div>
<hr/>


## The Problem
You to do some analysis in order to predict the crypto currency market. Crypto API allows
you to access the sentiments of tweets from Twitter between the start_date and end_date.


## This solution
The Crypto API is a very lightweight solution in order to help you to predict the crypto currency
market.

## Installation
Start by building a development environment

1. Install the dependencies of project
```
$ pip install -r requirements.txt
```
2. Create the environment variable file (.env) to include Twitter credentials
```
TWITTER_CONSUMER_KEY=""
TWITTER_CONSUMER_SECRET=""
TWITTER_ACCESS_TOKEN=""
TWITTER-ACCESS_TOKEN_SECRET=""
```
3. Run the Crypto API
```
$ python manage.py runserver
```

## Endpoints Structure
| Endpoint        | Method  | Description  |
| ------------- |:-------------:| :-----|
| /v0/crypto_analysis/     | POST      |   Create a new set of analysis |

### Endpoint Example
``` 
Request:
POST /v0/crypto_analysis/

{
    "crypto_currency": {
        "name": "BTC",
        "start_date": "2020-04-01",
        "end_date": "2020-04-10
    }
}

Response:
[
    {
        "sentence": "Bitcoin is a great option to invest!",
        "polarity": 1.0,
        "subjectivity": 0.75,
    }
]
```

## Errors
The Crypto API uses conventional HTTP response codes to indicate errors, and includes
more detailed information on the exact nature of an error in the HTTP response.

<hr/>

HTTP RESPONSE CODES
<hr/>

| RESPONSE CODE | MESSAGE    |
| ------------- |:----------:|
| 200 OK        | All is well|
| 201 CREATED   | A resource has been created |
| 400 BAD REQUEST | Your request has missing arguments |
| 405 METHOD NOT ALLOWED | You are using an incorrect HTTP verb |
| 404 NOT FOUND | The endpoint requested does not exist |
| 500 INTERNAL SERVER ERROR | Something is wrong on our end |
