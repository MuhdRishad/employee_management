from django.urls import path
from calculator import views

urlpatterns = [
    path("home",views.HomeView.as_view(),name="calc-home"),
    path("add",views.AddView.as_view(),name="calc-add"),
    path("sub",views.SubView.as_view(),name="calc-sub"),
    path("multi",views.MultyView.as_view(),name="calc-multi"),
    path("division",views.DivisionView.as_view(),name="calc-division"),
    path("exp",views.ExpView.as_view(),name="calc-exp"),
    path("mod",views.ModView.as_view(),name="calc-modules"),
    path("factorial",views.FactView.as_view(),name="calc-factorial"),
    path("wordcount",views.WordCountView.as_view(),name="calc-wordcount"),
    path("primenumber",views.PrimeNumberView.as_view(),name="calc-primenumber"),
]