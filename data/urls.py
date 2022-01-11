from django.urls import path
from .views import BtcUsdView

urlpatterns = [
    path('quotes/', BtcUsdView.as_view()),

]
