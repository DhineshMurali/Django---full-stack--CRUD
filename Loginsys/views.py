from django import forms
from django.shortcuts import render
from Loginsys.forms import recforms
from Loginsys.models import Newuser
from Loginsys.models import editUpdateRecord
from django.contrib import messages


def Indexpage(request):
    return render(request, 'index.html')


def Userreg(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Email = request.POST['Email']
        Pwd = request.POST['Pwd']
        Age = request.POST['Age']
        Gender = request.POST['Gender']
        MartialStatus = request.POST['MartialStatus']
        Newuser(Username=Username, Email=Email, Pwd=Pwd, Age=Age,
                Gender=Gender, MartialStatus=MartialStatus).save()
        messages.success(request, 'The new user ' +
                         request.POST['Username']+' is saved successfully')
        return render(request, 'registration1.html')
    else:
        return render(request, 'registration1.html')


def loginpage(request):
    if request.method == "POST":
        try:
            Userdetails = Newuser.objects.get(
                Email=request.POST['Email'], Pwd=request.POST['Pwd'])
            print("Username= ", Userdetails)
            request.session['Email'] = Userdetails.Email
            return render(request, 'index.html')
        except Newuser.DoesNotExist as e:
            messages.success(request, 'Username/Password Invalid')
    return render(request, 'Login.html')


def logout(request):
    try:
        del request.session['Email']
    except:
        return render(request, 'Index.html')
    return render(request, 'Index.html')


def displaydata(request):
    results = editUpdateRecord.objects.all()
    return render(request, "index2.html", {"editUpdateRecord": results})


def editrec(request, id):
    displayrec = editUpdateRecord.objects.get(id=id)
    return render(request, "edit.html", {"editUpdateRecord": displayrec})


def updaterec(request, id):
    updaterec = editUpdateRecord.objects.get(id=id)
    form = recforms(request.POST, instance=updaterec)
    if form.is_valid:
        form.save()
        messages.success(request, "Record upadted successfully")
        return render(request, "edit.html", {"editUpadateRecord": updaterec})
