from django.shortcuts import render
from .serializers import RegisterSerializer
# Create your views here.
from rest_framework import generics,status
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
class RegisterView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

@api_view(['GET','POST'])
@permission_classes(AllowAny,)
def protected_route(request):
    if request.method == 'GET':
        resp = f'Hey, {request.user}, You are logged in'

        return Response({"response":resp},status = status.HTTP_200_ok)
    
    elif request.method == 'POST':
        resp = f"Hey,{request.user},you are just fine"
        return Response({"response":resp},status=status.HTTP_201_CREATED)
    return Response({},status=status.HTTP_400_BAD_REQUEST)
        

