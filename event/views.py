from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import EventSerializer,EventSerializerUpdate
from .models import Event
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from localization.models import Localization
from game.models import Game
from user.models import User

class EventView(APIView):

    def post(self,request):

       
        try:
            localization = Localization.objects.get(uuid=request.data['localization_id'])
            print(localization)
            game = Game.objects.get(uuid=request.data['game_id'])

            serializer= EventSerializer(data=request.data)

            if not serializer.is_valid():
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
          
            event = Event.objects.get_or_create(**serializer.validated_data)
            event[0].localization = localization
            event[0].game = game
            event[0].save()
           
            return Response(EventSerializer(event[0]).data,status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist:
                Response({"message":"game or localization does not exist"},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,event_id=''):
        if event_id:
            try:
                event = Game.objects.get(uuid=event_id)
                serializer = EventSerializer(event)

                return Response(serializer.data,status=status.HTTP_200_OK)

            except ObjectDoesNotExist:
                Response({"message":"Event does not exist"},status=status.HTTP_404_NOT_FOUND )
        
        event =  Event.objects.all()
        serializer = EventSerializer(event,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def patch(self,request,event_id=''):
        try:
          
            event = Event.objects.filter(uuid=event_id).first()

            serializer=EventSerializerUpdate(data=request.data)
            if not serializer.is_valid():
                     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

            try:
                users_id = request.data['user_id']
                for user_id in users_id:
                    user = User.objects.filter(id=user_id).first()
                    if user == None:
                        return Response({"message":"User does not exist"},status=status.HTTP_404_NOT_FOUND)
            except ObjectDoesNotExist:
                Response({"message":"User does not exist"},status=status.HTTP_404_NOT_FOUND )
            if 'user_id' in request.data:
                event.users.set(request.data['user_id'])
            
                
            for field,value in serializer.validated_data.items():
                setattr(event,field,value)
            
            event.save()
            serializer=EventSerializerUpdate(event)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
                Response({"message":"Event does not exist"},status=status.HTTP_404_NOT_FOUND )
        except IntegrityError:
            Response({"message":"User does not exist"},status=status.HTTP_404_NOT_FOUND )

