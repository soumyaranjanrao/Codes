from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from empdetails.models import Employee
from empdetails.serializers import EmployeeSerializer

# Create your views here.
class EmployeeList(APIView):
    def get(self,request):
        lst = get_list_or_404(Employee)
        slst = EmployeeSerializer(lst,many=True)
        return Response(slst.data)

    def post(self,request):
        sobj = EmployeeSerializer(data=request.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data,status=status.HTTP_201_CREATED)
        else:
            return Response(sobj.error,status=status.HTTP_400_BAD_REQUEST)

class EmployeeModify(APIView):
    def get_object(self,id):
        try:
            return get_object_or_404(Employee,id=id)
        except:
            return Response({'error':'Employee details not found'},status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        emp = self.get_object(id)
        sobj = EmployeeSerializer(emp)
        return Response(sobj.data)

    def put(self,request,id):
        emp = self.get_object(id)
        sobj = EmployeeSerializer(emp,data=request.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data,status=status.HTTP_200_OK)
        else:
            return Response(sobj.error,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        emp = self.get_object(id)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

