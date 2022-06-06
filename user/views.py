from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from user.models import User
from .serializers import UserSerializer,UserSerializerUpdate
from django.core.exceptions import ObjectDoesNotExist

class UserView(APIView):

    def post(self,request):

        data = request.data

        serializer = UserSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        ids = User.objects.all()
       
        user = User.objects.create(**serializer.validated_data)
        user_output = ids[len(ids)-1]
        return Response(UserSerializer(user_output).data, status=status.HTTP_201_CREATED)

    
    def get(self,request,user_id=''):
        
        if user_id:
            try:
                id = int(user_id)
                user = User.objects.get(id=id)
                serializer = UserSerializer(user)

                return Response(serializer.data,status=status.HTTP_200_OK)

            except ObjectDoesNotExist:
                Response({"message":"user does not exist"},status=status.HTTP_404_NOT_FOUND )
        
        users =  User.objects.all()
        serializer = UserSerializer(users,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def patch(self,request,user_id=""):
        try:
            id = int(user_id)
            user = User.objects.get(id=id)
            serializer=UserSerializerUpdate(data=request.data)
            if not serializer.is_valid():
                     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

            for field,value in serializer.validated_data.items():
                setattr(user,field,value)

            user.save()
            serializer= serializer = UserSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
                Response({"message":"user does not exist"},status=status.HTTP_404_NOT_FOUND )
    
    def delete(self,request,user_id=""):
        try:
            id = int(user_id)
            user = User.objects.get(id=id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENTS)
        except ObjectDoesNotExist:
                Response({"message":"user does not exist"},status=status.HTTP_404_NOT_FOUND )
    
        







