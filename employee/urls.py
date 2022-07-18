from django.urls import path
from employee import views


# FUNCTION BASED VIEW
# urlpatterns = [
#     path('index',views.index),
#     path('login',views.login),
#     path('registration',views.registration),
# ]


#CLASS BASED VIEW
urlpatterns = [
    path("",views.index,name="index"),
    path('add',views.EmployeeCreateView.as_view(),name="emp-add"),
    path('all',views.EmployeeListView.as_view(),name="emp-list"),
    path('details/<str:eid>',views.EmployeeDetailView.as_view(),name="emp-detail"),
    path('change/<str:eid>',views.EmployeeEditView.as_view(),name="emp-edit"),
    path('remove/<str:eid>',views.remove_employee,name="emp-remove"),
    path('accounts/signup',views.SignUpView.as_view(),name="sign-up"),
    path('accounts/signin',views.UserLogInView.as_view(),name="sign-in"),
    path("accounts/signout",views.sign_out,name="signout")
]
