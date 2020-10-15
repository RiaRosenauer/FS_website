from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin', admin.site.urls),
    path('exerciseSet', views.set_of_exercises, name='set_of_exercises'),
    path('favourites', views.favourites, name='favourites'),
    path('toRepeat', views.to_repeat, name='to_repeat'),
    path('exerciseSet/<int:pk>',views.exercise_view, name='exercise_view'),
    
]