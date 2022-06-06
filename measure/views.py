from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import MeasureSerializer
from .models import Measure
from django.core.exceptions import ObjectDoesNotExist
from user.models import User

class MeasureView(APIView):

    def post(self,request):

        user_id = int(request.data['user_id'])
        try:
            user = User.objects.get(id=user_id)
            serializer= MeasureSerializer(data=request.data)

            if not serializer.is_valid():
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
          
            measure = Measure.objects.create(**serializer.validated_data)
            measure.user = user
            measure.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist:
                Response({"message":"user does not exist"},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,measure_id=''):
        if measure_id:
            try:
                measure = Measure.objects.get(uuid=measure_id)
                serializer = MeasureSerializer(measure)

                return Response(serializer.data,status=status.HTTP_200_OK)

            except ObjectDoesNotExist:
                Response({"message":"measure does not exist"},status=status.HTTP_404_NOT_FOUND )
        
        measure =  Measure.objects.all()
        serializer = MeasureSerializer(measure,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def patch(self,request,measure_id=''):
        try:
          
            measure = Measure.objects.get(uuid=measure_id)
            serializer=MeasureSerializer(data=request.data)
            if not serializer.is_valid():
                     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

            for field,value in serializer.validated_data.items():
                setattr(measure,field,value)

            measure.save()
            serializer= MeasureSerializer(measure)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
                Response({"message":"measure does not exist"},status=status.HTTP_404_NOT_FOUND )

    def delete(self,request,measure_id=""):
        try:
            
            measure = Measure.objects.filter(uuid=measure_id).first()
         
            if measure == None:
                return Response({"message":"measure does not exist"},status=status.HTTP_404_NOT_FOUND)

            measure.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
                Response({"message":"measure does not exist"},status=status.HTTP_404_NOT_FOUND)
        except AttributeError:
               Response({"message":"measure does not exist"},status=status.HTTP_404_NOT_FOUND)