import pytest

from data.models import BtcUsd


class TestModels():

    @pytest.mark.django_db
    def test_btc_usd_model_creation(self):
        btcusd = BtcUsd.objects.create(
            from_currency_code='BTC',
            to_currency_code='USD',
            exchange_rate=45000.22,
            date="2022-01-11T23:59:10Z",
            time_zone='UTC',
            bid_price=41111.11,
            ask_price=46666.66
        )
        assert BtcUsd.objects.count() == 1
        assert btcusd.from_currency_code == 'BTC'
