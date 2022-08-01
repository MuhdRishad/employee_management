from employee.models import Employee
from rest_framework import serializers


class EmoloyeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate(self, data):
        salary = data.get("emp_salary")
        experience = data.get("emp_experience")
        if salary < 0 or experience < 0:
            raise serializers.ValidationError("invalid salary or experience")
        return data


