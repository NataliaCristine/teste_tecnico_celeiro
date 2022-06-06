from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import TeamSerializer,TeamSerializerUpdate
from .models import Team
from django.core.exceptions import ObjectDoesNotExist
from user.models import User

class TeamView(APIView):

    def post(self,request):

        user_id = int(request.data['user_id'])
        try:
            user = User.objects.get(id=user_id)
            serializer= TeamSerializer(data=request.data)

            if not serializer.is_valid():
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
          
            team = Team.objects.get_or_create(**serializer.validated_data)
            user.team = team[0]
            user.save()

            return Response(TeamSerializer(team[0]).data,status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist:
                Response({"message":"user does not exist"},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,team_id=''):
        if team_id:
            try:
                team = Team.objects.get(uuid=team_id)
                serializer = TeamSerializer(team)

                return Response(serializer.data,status=status.HTTP_200_OK)

            except ObjectDoesNotExist:
                Response({"message":"Team does not exist"},status=status.HTTP_404_NOT_FOUND )
        
        team =  Team.objects.all()
        serializer = TeamSerializer(team,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def patch(self,request,team_id=''):
        try:
          
            team = Team.objects.get(uuid=team_id)
            serializer=TeamSerializerUpdate(data=request.data)
            if not serializer.is_valid():
                     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

            for field,value in serializer.validated_data.items():
                setattr(team,field,value)

            team.save()
            serializer=TeamSerializerUpdate(team)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
                Response({"message":"Team does not exist"},status=status.HTTP_404_NOT_FOUND )

    def delete(self,request,team_id=""):
        try:
            
            team = Team.objects.filter(uuid=team_id).first()
            
            if team == None:
                return Response({"message":"Team does not exist"},status=status.HTTP_404_NOT_FOUND)

            team.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
                Response({"message":"Team does not exist"},status=status.HTTP_404_NOT_FOUND)
        except AttributeError:
               Response({"message":"Team does not exist"},status=status.HTTP_404_NOT_FOUND)

    