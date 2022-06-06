from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import PrizeSerializer
from .models import Prize
from django.core.exceptions import ObjectDoesNotExist
from user.models import User
from event.models import Event

class PrizeView(APIView):

    def post(self,request):

        user_id = int(request.data['user_id'])
        try:
            user = User.objects.get(id=user_id)
            event = Event.objects.get(uuid=request.data['event_id'])
            serializer= PrizeSerializer(data=request.data)

            if not serializer.is_valid():
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
          
            prize = Prize.objects.create(**serializer.validated_data)
            prize.user = user
            prize.event= event
            prize.save()


            return Response(serializer.data,status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist:
                Response({"message":"user does not exist"},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,prize_id=''):
        if prize_id:
            try:
                prize = Prize.objects.get(uuid=prize_id)
                serializer = PrizeSerializer(prize)

                return Response(serializer.data,status=status.HTTP_200_OK)

            except ObjectDoesNotExist:
                Response({"message":"prize does not exist"},status=status.HTTP_404_NOT_FOUND )
        
        prize =  Prize.objects.all()
        serializer = PrizeSerializer(prize,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def patch(self,request,prize_id=''):
        try:
          
            prize = Prize.objects.get(uuid=prize_id)
            serializer=PrizeSerializer(data=request.data)
            if not serializer.is_valid():
                     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

            for field,value in serializer.validated_data.items():
                setattr(prize,field,value)

            prize.save()
            serializer= PrizeSerializer(prize)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
                Response({"message":"prize does not exist"},status=status.HTTP_404_NOT_FOUND )

    def delete(self,request,prize_id=""):
        try:
            
            prize = Prize.objects.filter(uuid=prize_id).first()
         
            if prize == None:
                return Response({"message":"prize does not exist"},status=status.HTTP_404_NOT_FOUND)

            prize.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
                Response({"message":"prize does not exist"},status=status.HTTP_404_NOT_FOUND)
        except AttributeError:
               Response({"message":"prize does not exist"},status=status.HTTP_404_NOT_FOUND)
