import requests
from celery import shared_task

from core.settings import env
from data.serializers import BtcUsdSerializer


def get_data(date=None):
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={env('ALPHA_VANTAGE_API_KEY')}"
    r = requests.get(url)
    data = r.json()
    c_data = {
        'from_currency_code': data['Realtime Currency Exchange Rate']['1. From_Currency Code'],
        'to_currency_code': data['Realtime Currency Exchange Rate']['3. To_Currency Code'],
        'exchange_rate': data['Realtime Currency Exchange Rate']['5. Exchange Rate'],
        'date': data['Realtime Currency Exchange Rate']['6. Last Refreshed'],
        'time_zone': data['Realtime Currency Exchange Rate']['7. Time Zone'],
        'bid_price': data['Realtime Currency Exchange Rate']['8. Bid Price'],
        'ask_price': data['Realtime Currency Exchange Rate']['9. Ask Price'],
    }
    return c_data

@shared_task
def save_data():
    data = get_data()
    serializer = BtcUsdSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
