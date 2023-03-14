from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
   path('', views.homepage, name="homepage"),
   path('func/', views.fbview, name="func"),
   path('clas/', views.cbview.as_view(), name="clas"),
   path('fbvtemp/', views.fbtemp, name="fbvtemp"),
   path('cbvtemp/', views.cbtemp.as_view(), name="cbvtemp"),
   path('cfunc/', views.contactfunc, name="cfunc"),
   path('cclas', views.contactclas.as_view(), name='cclas')
]