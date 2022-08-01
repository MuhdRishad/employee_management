from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("employees",views.EmployeeViewsetsView,basename="employees")
router.register("memployees",views.EmployeeModelViewsetView,basename="memployees")

urlpatterns = [
    path('employees/',views.EmployeesView.as_view()),
    path('employee/<int:eid>',views.EmployeeDetailView.as_view()),
    path('employee/authtoken',obtain_auth_token)
]+router.urls
