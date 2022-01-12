# coinmena assignement

Requirements <br>
python 3.10 <br>
django  4.0 <br>
django rest framework 3.13  <br>
celery 5.2.3

## Instalation
Clone the repo and enter command <br/>
<strong>docker-compose up --build</strong>

## About

The app is designed to retreive data from alphavantage API for BTC/USD pair
every hour. <br>
To retreive all data stored in database send GET request to <br>
<strong>localhost:8000/api/v1/quotes/</strong> <br>
To view current market data send POST request to <br>
<strong>localhost:8000/api/v1/quotes/</strong>

## Tests
To start tests <br>
<strong>docker-compose run app pytest</strong>
