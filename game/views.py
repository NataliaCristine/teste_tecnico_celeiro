from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import GameSerializer,GameSerializerUpdate
from .models import Game
from django.core.exceptions import ObjectDoesNotExist


class GameView(APIView):

    def post(self,request):

       
        try:
            serializer= GameSerializer(data=request.data)

            if not serializer.is_valid():
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
          
            game = Game.objects.get_or_create(**serializer.validated_data)
           
            return Response(GameSerializer(game[0]).data,status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist:
                Response({"message":"game does not exist"},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,game_id=''):
        if game_id:
            try:
                game = Game.objects.get(uuid=game_id)
                serializer = GameSerializer(game)

                return Response(serializer.data,status=status.HTTP_200_OK)

            except ObjectDoesNotExist:
                Response({"message":"Game does not exist"},status=status.HTTP_404_NOT_FOUND )
        
        game =  Game.objects.all()
        serializer = GameSerializer(game,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def patch(self,request,game_id=''):
        try:
          
            game = Game.objects.get(uuid=game_id)

            serializer=GameSerializerUpdate(data=request.data)
            if not serializer.is_valid():
                     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            if 'team_id' in request.data:
                game.teams.set(request.data['team_id'])

            for field,value in serializer.validated_data.items():
                setattr(game,field,value)

            game.save()
            serializer=GameSerializerUpdate(game)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
                Response({"message":"Game does not exist"},status=status.HTTP_404_NOT_FOUND )

   
