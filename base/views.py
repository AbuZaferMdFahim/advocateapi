from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocate
from base.serilaizers import AdvocateSerializers
from django.db.models import Q

# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data = ['/advocates','advocates/:username']
    return Response(data)

@api_view(['GET'])
def advocate_list(request):
    query = request.GET.get('query')
    if query == None:
        query =''
    advocates = Advocate.objects.filter(Q(username__icontains = query) | Q(bio_icontains = query))
    serializers = AdvocateSerializers(advocates,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def advocate_details(request,username):
    # data = username
    advocate = Advocate.objects.get(username=username)
    serializers = AdvocateSerializers(advocate,many=False)
    return Response(serializers.data)