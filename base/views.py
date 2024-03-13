from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Advocate,Company
from .serilaizers import AdvocateSerializers


# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data = ['/advocates','advocates/:username']
    return Response(data)

# function base view [S]
# @api_view(['GET','POST'])
# def advocate_list(request):
#     if request.method == 'GET':
#         query = request.GET.get('query')
#         if query == None:
#             query =''
#         advocates = Advocate.objects.filter(Q(username__icontains = query) | Q(bio__icontains = query))
#         serializers = AdvocateSerializers(advocates,many=True)
#         return Response(serializers.data)
#     if request.method == 'POST':
#         advocate = Advocate.objects.create(username = request.data['username'],bio=request.data['bio'])
#         serializers = AdvocateSerializers(advocate,many=False)
#         return Response(serializers.data)

# @api_view(['GET','PUT','DELETE'])
# def advocate_details(request,username):
#     # data = username
#     advocate = Advocate.objects.get(username=username)
#     if request.method == "GET":
#         serializers = AdvocateSerializers(advocate,many=False)
#         return Response(serializers.data)
    
#     if request.method=='PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
#         advocate.save()
#         serializers = AdvocateSerializers(advocate,many=False)
#         return Response(serializers.data)
    
#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response('User Deleted')
# function base view [E]

#class Based view [S]
class AdvocateList(APIView):
    def get(self,request):
        query = request.GET.get('query')
        if query == None:
            query =''
        advocates = Advocate.objects.filter(Q(username__icontains = query) | Q(bio__icontains = query))
        serializers = AdvocateSerializers(advocates,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        advocate = Advocate.objects.create(username = request.data['username'],bio=request.data['bio'])
        serializers = AdvocateSerializers(advocate,many=False)
        return Response(serializers.data)


class AdvocateDetails(APIView):
    
    def get_object(self,username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise JsonResponse("Advocate Does not Exist")
        
    def get(self,request,username):
        advocate = self.get_object(username)
        serializers = AdvocateSerializers(advocate,many=False)
        return Response(serializers.data)

    def put(self,request,username):
        advocate = self.get_object(username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        serializers = AdvocateSerializers(advocate,many=False)
        return Response(serializers.data)
    
    def delete(self,request,username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response('User Deleted')
#class Based view [E]   

@api_view(['GET'])
def companies_list(request):     
    return Response()