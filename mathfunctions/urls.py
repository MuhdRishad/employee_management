from django.urls import path
from mathfunctions import views

urlpatterns = [
    path("home",views.HomeView.as_view(),name="math-home"),
    path("add",views.AdditionView.as_view(),name="math-add"),
    path("sub",views.SubstractionView.as_view(),name="math-sub"),
    path("mul",views.MultiplicationView.as_view(),name="math-multi"),
    path("div",views.DivisionView.as_view(),name="math-div"),

]