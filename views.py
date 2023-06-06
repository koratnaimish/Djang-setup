from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view



# Create your views here.
@api_view(['POST'])
def index(request):
    try:
       if request.method == 'POST':
           datas = request.data
           serializer = UserSerializer(data=datas)
           if serializer.is_valid():
               serializer.save()
               return JsonResponse(serializer.data)
           return JsonResponse(serializer.errors)
    except Exception as e:
        return JsonResponse({'message':e.args,'code':500})

