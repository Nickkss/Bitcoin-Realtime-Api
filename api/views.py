from django.shortcuts import render

from rest_framework.authtoken import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator

import requests

from .models import Bitcoin
from .serializers import BitcoinSerializer

# Create your views here.
class GetBitcoinPriceView(views.APIView):
    permission_classes = (IsAuthenticated,)
    
    # def get(self, request):
    #     context = {'message':'hello world'}
    #     return Response(context)
    
    def post(self, request):
        
        try:
            page_number = self.request.query_params.get('page_number', 1)
            page_size = self.request.query_params.get('page_size', 10)
                
            url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
            response = requests.get(url)
            if response.status_code == 200:
                json_data = response.json()
                Bitcoin.objects.create(symbol=json_data['symbol'], price=float(json_data['price']))
                bitcoins = Bitcoin.objects.all()
                paginator = Paginator(bitcoins , page_size)
                serializer = BitcoinSerializer(paginator.page(page_number), many=True, context={'request':request})
                data = {'succ':True, 'msg':'Price fetched.', 'data':serializer.data}
            else:
                data = {'succ':False, 'msg':'Unable to get price data.'}
        except Exception as ex:
            print(ex)
            data = {'succ':False, 'msg':'Unable to get price data.'}
        return Response(data)
            