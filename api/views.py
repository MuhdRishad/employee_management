from django.shortcuts import render
from employee.models import Employee
from api.serializers import EmoloyeesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions,authentication


# Create your views here.

#  USING MODEL SERIALIZER
class EmployeesView(APIView):
    serializer_class = EmoloyeesSerializer

    def get(self,request,*args,**kwargs):
        all_employees = Employee.objects.all()
        serializer = self.serializer_class(all_employees,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class EmployeeDetailView(APIView):
    serializer_class = EmoloyeesSerializer

    def get(self,request,*args,**kwargs):
        emp_id = kwargs.get('eid')
        try:
            emp = Employee.objects.get(id=emp_id)
            serializer = self.serializer_class(emp)
            return Response(data=serializer.data)
        except:
            return Response({"message":"invalid"},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,*args,**kwargs):
        emp_id = kwargs.get('eid')
        instance = Employee.objects.get(id=emp_id)
        serializer = self.serializer_class(data=request.data,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        emp_id = kwargs.get('eid')
        try:
            emp = Employee.objects.get(id=emp_id)
            emp.delete()
            return Response(data=request.data)
        except:
            return Response({"message":"invalid"},status=status.HTTP_400_BAD_REQUEST)





#     USING VIEWSET
class EmployeeViewsetsView(viewsets.ViewSet):
    serializer_class = EmoloyeesSerializer

    def list(self,request,*args,**kwargs):
        all_employees = Employee.objects.all()
        serializer = self.serializer_class(all_employees,many=True)
        return Response(data=serializer.data)

    def create(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def retrieve(self,request,*args,**kwargs):
        emp_id = kwargs.get("pk")
        try:
            employee = Employee.objects.get(id=emp_id)
            serializer = self.serializer_class(employee)
            return Response(data=serializer.data)
        except:
            return Response({"msg":"invalid"},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,*args,**kwargs):
        emp_id = kwargs.get("pk")
        instance = Employee.objects.get(id=emp_id)
        serializer = self.serializer_class(instance=instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        emp_id = kwargs.get("pk")
        employee = Employee.objects.get(id=emp_id)
        employee.delete()
        return Response({"msg":"deleted"})



#  USING MODELVIEWSET
class EmployeeModelViewsetView(viewsets.ModelViewSet):
    serializer_class = EmoloyeesSerializer
    queryset = Employee.objects.all()
    model = Employee
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]



