import pytest
from django.urls import reverse

from data.views import BtcUsdView


class TestViews():

    @pytest.mark.django_db
    def test_usd_btc_get_view(self, rf):
        request = rf.get(reverse('api:quotes_view'))
        response = BtcUsdView.as_view()(request)
        assert response.status_code == 200

    def test_usd_btc_post_view(self, rf):
        request = rf.post(reverse('api:quotes_view'))
        response = BtcUsdView.as_view()(request)
        assert response.status_code == 200
