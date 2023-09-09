from user_api.models import User
from services.models import Service
from services.serializers import ServiceSerializer
from user_api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework import status
from django.db.models import Count



# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)    
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs) 
    
class UserAddService(APIView):
    
    def get_user(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def post(self,request,pk):
       data=JSONParser().parse(request)
       user = self.get_user(pk)
       services = Service.objects.filter(pk__in=data["services"])
       user.services.set(services )
       
       return Response({"success":True})
          
class FacultyGroup(APIView):
    
    def get(self,request):
        faculty_count = User.objects.values('faculty').annotate(count=Count('faculty'))
        faculty_count_dict = {item['faculty']:item['count'] for item in faculty_count}
        return Response(faculty_count_dict)       
            