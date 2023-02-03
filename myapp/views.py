from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StripePaymentSerializer
from rest_framework.response import Response

# Create your views here.


import stripe
stripe.api_key = "sk_test_51MWwXOSIfm4NPswUnHyASDs6bqzfIBbSTvd8OmSes7mZyp987hHFlVwsTB9QUoKgkZMO8Oxqd2rEMG9nHEvRudBQ00msCJFwz6"

class StripePaymentView(APIView):
    def post(self, request, format=None):
        serializer = StripePaymentSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)