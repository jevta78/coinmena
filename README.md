# coinmena assignement

Requirements <br>
python 3.10 <br>
django  4.0 <br>
django rest framework 3.13  <br>
celery 5.2.3

## Instalation
Clone the repo <br/>
```shell
cp .env.copy .env
```
```shell
docker-compose up --build
```

## About

The app is designed to retreive data from alphavantage API for BTC/USD pair
every hour. <br>
To retreive all data stored in database send GET request to <br>
```shell
localhost:8000/api/v1/quotes/
```

To view current market data send POST request to <br>
```shell
localhost:8000/api/v1/quotes/
```

## Tests
To start tests <br>
<strong>docker-compose run app pytest</strong>
