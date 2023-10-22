
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.train),
    path('feedback/', views.feedback),
    #path('thanks/', views.thanks),
]