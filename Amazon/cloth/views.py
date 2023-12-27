from django.shortcuts import render
from .models import stud_detail
from .serializer import serializ_stud
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class stud_api(APIView):
    def get(self,r):
        q_obj=stud_detail.objects.all()
        ser_obj=serializ_stud(q_obj,many=True)
        return Response(ser_obj.data)
    def post(self,r):
        ser_obj=serializ_stud(data=r.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return status.is_client_error()
class update(APIView):
    def put(self,r,id):
        obj=stud_detail.objects.get(id=id)
        ser_obj=serializ_stud(obj,data=r.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return status.is_client_error()
    def delete(self,r,id):
        obj=stud_detail.objects.get(id=id)
        obj.delete()
        return status.HTTP_202_ACCEPTED
