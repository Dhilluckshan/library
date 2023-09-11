from user_api.models import User
from services.models import Service
from services.serializers import ServiceSerializer
from user_api.serializers import UserSerializer, UserRegistrationSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework import status
from django.db.models import Count
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class UserRegister(APIView):

    def post(self, request):
        reg_serializer = UserRegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserAddService(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        user = request.user
        services = Service.objects.filter(pk__in=data["services"])
        user.services.set(services)

        return Response({"success": True})


class FacultyGroup(APIView):

    def get(self, request):
        faculty_count = User.objects.values(
            'faculty').annotate(count=Count('faculty'))
        faculty_count_dict = {item['faculty']: item['count']
                              for item in faculty_count}
        return Response(faculty_count_dict)


class LoginUser(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("reg_number")
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            # If the user is authenticated, create and return JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token,
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
