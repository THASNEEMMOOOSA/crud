from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from poll.models import Person
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())


def persons(request):
    template=loader.get_template('persons.html')
    p=Person.objects.all()
    context={
        'p':p
    }

    return HttpResponse(template.render(context,request))


def pdetails(request,id):
    template=loader.get_template('pdetails.html')
    p=Person.objects.get(id=id)
    context={
        'p':p
    }

    return HttpResponse(template.render(context,request))



def adduserpage(request):
    template=loader.get_template('adduserpage.html')
 

    return HttpResponse(template.render())

@csrf_exempt
def registeruser(request):
    template=loader.get_template('addsuccess.html')
    if request.method=='POST':
        name=request.POST['name']
        eid=request.POST['eid']
        email=request.POST['email']
        mob=request.POST['mob']
        address=request.POST['address']
        prof=request.POST['prof']
        age=request.POST['age']



        print(name,eid,email,mob,address,prof)
        person=Person(name=name,email=email,eid=eid,mob=mob,address=address,prof=prof,age=age)
        person.save()
    


    return HttpResponse(template.render())


def delete(request,id):
    template=loader.get_template('deletesuccess.html')
    p=Person.objects.get(id=id)
    p.delete()

    return HttpResponse(template.render())


def update(request,id):
    template=loader.get_template('updatepage.html')
    p=Person.objects.get(id=id)
    context={
        'p':p
    }

 

    return HttpResponse(template.render(context,request))
@csrf_exempt
def updateprocess(request,id):
    template=loader.get_template('updatesuccess.html')
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        prof=request.POST['prof']
        age=request.POST['age']



        print(name,email,address,prof)
        p=Person.objects.get(id=id)
        p.name=name
        p.email=email
        p.address=address
        p.prof=prof
        p.age=age


        p.save()
    context={
        'p':p
    }


    return HttpResponse(template.render(context,request))
