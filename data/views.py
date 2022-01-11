from rest_framework.views import APIView
from rest_framework.response import Response

from data.models import BtcUsd
from data.serializers import BtcUsdSerializer
from data.tasks import get_data


class BtcUsdView(APIView):
    def get(self, request):
        data=BtcUsd.objects.all()
        ser=BtcUsdSerializer(data, many=True)
        return Response(ser.data)

    def post(self, request):
        data = get_data()
        serializer = BtcUsdSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)