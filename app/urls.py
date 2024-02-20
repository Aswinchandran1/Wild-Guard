from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index),
    path('login',views.login),
    path('register',views.register),

    path('forestdivision',views.forest_division),
    path('update_division/<id>',views.update_division),
    path('delete_division/<id>',views.delete_division),

    path('foreststation',views.forest_station),
    path('update_station/<id>',views.update_station),
    path('delete_station/<id>',views.delete_station),

    path('forestofficer',views.admin_manage_forest_officer),
    path('update_officer/<id>',views.update_officer),
    path('delete_officer/<id>',views.delete_officer),

    path('animals',views.animal_managment),
    path('update_animals/<id>',views.update_animals),
    path('delete_animals/<id>',views.delete_animals),

    path('notifications',views.send_notification),
    path('delete_notification/<id>',views.delete_notification),
]