from django.urls import path
from .views import BtcUsdView

app_name='api'

urlpatterns = [
    path('quotes/', BtcUsdView.as_view(), name='quotes_view'),

]
