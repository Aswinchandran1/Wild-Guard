from django.http import HttpResponse
from django.shortcuts import render
from . models import *
# Create your views here.


def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
    
#ADMIN HOME
def admin_home(request):
     return render(request,'admin/admin_home.html')

#END OFADMIN HOME
#MANAGE FOREST DIVISION   
def forest_division(request):
    q2=Forest_Division.objects.all()
    if 'submit' in request.POST:
        division_name=request.POST['division_name']
        q1=Forest_Division(division_name=division_name)
        q1.save()
        return HttpResponse("<script>alert('added.....');window.location='/forestdivision'</script>")
    return render(request,'admin/admin_manage_forest_division.html',{'q2':q2})

def update_division(request,id):
    q3=Forest_Division.objects.get(id=id)
    if 'update' in request.POST:
            division_name=request.POST['division_name']
            q3.division_name=division_name
            q3.save()
            return HttpResponse("<script>alert('updated.....');window.location='/forestdivision'</script>")
    return render(request,'admin/admin_manage_forest_division.html',{'q3':q3})

def delete_division(request,id):
    q4=Forest_Division.objects.get(id=id)
    q4.delete()
    return HttpResponse("<script>alert('deleted.....');window.location='/forestdivision'</script>")
# END OF MANAGE FOREST DIVISION   

#MANAGE FOREST STATION
def forest_station(request):
    q1=Forest_Division.objects.all()
    q3=Forest_Station.objects.all()
    if 'submit' in request.POST:
        division_name=request.POST['division_name']
        station_name=request.POST['station_name']
        place=request.POST['place']
        contact_number=request.POST['contact_number']
        q2=Forest_Station(station_name=station_name,place=place,contact_number=contact_number,FOREST_DIVISION_id=division_name)
        q2.save()
        return HttpResponse("<script>alert('added.....');window.location='/foreststation'</script>")
    return render(request,'admin/admin_manage_forest_station.html',{'q1':q1,'q3':q3})

def update_station(request,id):
    q5=Forest_Division.objects.all()
    q4=Forest_Station.objects.get(id=id)
    if 'update' in request.POST:
        division_name=request.POST['division_name']
        station_name=request.POST['station_name']
        place=request.POST['place']
        contact_number=request.POST['contact_number']
        q4.FOREST_DIVISION_id=division_name
        q4.station_name=station_name
        q4.place=place
        q4.contact_number=contact_number
        q4.save()
        return HttpResponse("<script>alert('updated.....');window.location='/foreststation'</script>")
    return render(request,'admin/admin_manage_forest_station.html',{'q4':q4,'q5':q5})

def delete_station(request,id):
    q6=Forest_Station.objects.get(id=id)
    q6.delete()
    return HttpResponse("<script>alert('deleted.....');window.location='/foreststation'</script>")
#END OF MANAGE FOREST STATION

#MANAGE ANIMALS
def animal_managment(request):
    q1=Forest_Division.objects.all()
    q3=Animal.objects.all()
    if 'submit' in request.POST:
        division_name=request.POST['division_name']
        animal_name=request.POST['animal_name']
        animal_image=request.FILES['animal_image']
        description=request.POST['description']
        safety_tips=request.POST['safety_tips']
        q2=Animal(animal_name=animal_name,animal_image=animal_image,animal_description=description,safety_tips=safety_tips,FOREST_DIVISION_id=division_name)
        q2.save()
        return HttpResponse("<script>alert('added.....');window.location='/animals'</script>")
    return render(request,'admin/admin_manage_animal.html',{'q1':q1,'q3':q3})

def update_animals(request,id):
    q5=Forest_Division.objects.all()
    q4=Animal.objects.get(id=id)
    if 'update' in request.POST:
        division_name=request.POST['division_name']
        animal_name=request.POST['animal_name']
        animal_image=request.FILES['image']
        description=request.POST['description']
        safety_tips=request.POST['safety_tips']
        q4.FOREST_DIVISION_id=division_name
        q4.animal_name=animal_name
        q4.animal_image=animal_image
        q4.animal_description=description
        q4.safety_tips=safety_tips
        q4.save()
        return HttpResponse("<script>alert('updated.....');window.location='/animals'</script>")
    return render(request,'admin/admin_manage_animal.html',{'q4':q4,'q5':q5})
def delete_animals(request,id):
    q6=Animal.objects.get(id=id)
    q6.delete()
    return HttpResponse("<script>alert('deleted.....');window.location='/animals'</script>")
# END OF MANAGE ANIMALS

#MANAGE FOREST OFFFICER
def admin_manage_forest_officer(request):
    q3=Forest_Officer.objects.all()
    if 'submit' in request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        place = request.POST['place']
        phno = request.POST['phno']
        designation = request.POST['designation']
        email = request.POST['email']
        password = request.POST['password']
        q1=Login(username=email,password=password,usertype='forest_officer')
        q1.save()
        q2=Forest_Officer(fname=fname,lname=lname,place=place,phone=phno,designation=designation,email=email,LOGIN_id=q1.pk)
        q2.save()
        return HttpResponse("<script>alert('added.....');window.location='/forestofficer'</script>")
    return render(request,'admin/admin_manage_forest_officer.html',{'q3':q3})

def update_officer(request,id):
    q4=Forest_Officer.objects.get(id=id)
    if 'update' in request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        place = request.POST['place']
        phno = request.POST['phno']
        designation = request.POST['designation']
        q4.fname=fname
        q4.lname=lname
        q4.place=place
        q4.phone=phno
        q4.designation=designation
        q4.save()
        return HttpResponse("<script>alert('updated.....');window.location='/forestofficer'</script>")
    return render(request,'admin/admin_manage_forest_officer.html',{'q4':q4})

def delete_officer(request,id):
    q5=Forest_Officer.objects.get(id=id)
    q5.delete()
    return HttpResponse("<script>alert('deleted.....');window.location='/forestofficer'</script>")
#END OF MANAGE FOREST OFFICER

#NOTIFICATION
def send_notification(request):
    q2=Notification.objects.all()
    if 'submit' in request.POST:
        title=request.POST['title']
        description=request.POST['description']
        date=request.POST['date']
        q1=Notification(title=title,description=description,date=date)
        q1.save()
        return HttpResponse("<script>alert('added.....');window.location='/notifications'</script>")
    return render(request,'admin/admin_send_notification.html',{'q2':q2})

def delete_notification(request,id):
    q3=Notification.objects.get(id=id)
    q3.delete()
    return HttpResponse("<script>alert('deleted.....');window.location='/notifications'</script>")

#END NOTIFICATION

#complaints
def view_complaints(request):
    q2=Complaints.objects.all()
    return render(request,'admin/admin_view_complaints.html',{'q2':q2})

def send_replay(request):
    q3=Complaints.objects.get(id=id)
    if 'submit' in request.POST:
        replay=request.POST['replay']
        q3.reply=replay
        q3.save()
        return HttpResponse("<script>alert('replaied.....');window.location='/complaints'</script>")
    return render(request,'admin/admin_send_replay.html')