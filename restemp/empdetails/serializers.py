from rest_framework import serializers
from empdetails.models import Employee

#Write your serializers here
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
