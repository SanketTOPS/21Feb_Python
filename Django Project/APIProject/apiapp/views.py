from django.shortcuts import render
from .serializers import studSerializers
from .models import studInfo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def getalldata(request):
    if request.method=='GET':
        stdata=studInfo.objects.all()
        serial=studSerializers(stdata,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getid(request,id):
    try:
        stid=studInfo.objects.get(id=id)
    except studInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=studSerializers(stid)
    return Response(serial.data,status=status.HTTP_200_OK)

@api_view(['DELETE'])
def deleteid(request,id):
    try:
        stid=studInfo.objects.get(id=id)
    except studInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    studInfo.delete(stid)
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        stdata=studSerializers(data=request.data)
        if stdata.is_valid():
            stdata.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
