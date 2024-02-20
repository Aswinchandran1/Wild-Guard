from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=20)

class Forest_Officer(models.Model):
    LOGIN =models.ForeignKey(Login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)


class Forest_Division(models.Model):
    division_name=models.CharField(max_length=20)


class Forest_Station(models.Model):
    FOREST_DIVISION=models.ForeignKey(Forest_Division,on_delete=models.CASCADE)
    station_name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    contact_number=models.CharField(max_length=20)


class User(models.Model):
    LOGIN =models.ForeignKey(Login,on_delete=models.CASCADE)
    FOREST_STATION=models.ForeignKey(Forest_Station,on_delete=models.CASCADE)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=20)


class Animal(models.Model):
    FOREST_DIVISION=models.ForeignKey(Forest_Division,on_delete=models.CASCADE)
    animal_name=models.CharField(max_length=20)
    animal_image=models.ImageField(upload_to='static/animal')
    animal_description=models.CharField(max_length=20)
    safety_tips=models.CharField(max_length=20)
    
class Preserved_Animal(models.Model):
    ANIMAL=models.ForeignKey(Animal,on_delete=models.CASCADE)

class Complaints(models.Model):
     USER=models.ForeignKey(User,on_delete=models.CASCADE)
     title=models.CharField(max_length=20)
     description=models.CharField(max_length=20)
     reply=models.CharField(max_length=20)
     date=models.CharField(max_length=20)

class Notification(models.Model):
     title=models.CharField(max_length=20)
     description=models.CharField(max_length=20)
     date=models.CharField(max_length=20)


class Allocate(models.Model):
    FOREST_OFFICER=models.ForeignKey(Forest_Officer,on_delete=models.CASCADE)
    FOREST_STATION=models.ForeignKey(Forest_Station,on_delete=models.CASCADE)
    status=models.CharField(max_length=20)

class Alert(models.Model):
    description=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    alert_image=models.ImageField()
    
class Chat(models.Model):
    FOREST_OFFICER=models.ForeignKey(Forest_Officer,on_delete=models.CASCADE)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.CharField(max_length=20)
    date=models.CharField(max_length=20)

class Emergency_Message(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    message_image=models.CharField(max_length=20)
    description=models.CharField(max_length=20)

    


    


    




   