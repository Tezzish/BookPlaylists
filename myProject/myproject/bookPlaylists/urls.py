from django.urls import path
from . import views

urlpatterns = [
    #takes you to views.* after attaching / and the path
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.deleterecord, name='deleterecord')
]
