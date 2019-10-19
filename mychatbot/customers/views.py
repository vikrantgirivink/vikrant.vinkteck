from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Customer 
#from .serializers import *
#from rest_framework import viewsets, permissions
#from mychatbot import main
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
#from customers import main
#import json
from django.http import HttpResponse, JsonResponse

'''with open("/home/vikrant/Documents/chatbot/mychatbot/customers/intents.json") as file:
    data = json.load(file)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = CustomerSerializer'''


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def customer_chat(request, format=None):
    d=request.data
    if request.method == 'GET' or 'POST':
        if(len(d)!=0):
            dx=(list(d.values())[0])
            dt=check(dx)
            return Response({dt})
        else:
            return Response({'Give Data'})


def check(str):
    if(str=='hii' or 'hello'):
        return 'hello handsome'
    else:
        return('No DATA')

