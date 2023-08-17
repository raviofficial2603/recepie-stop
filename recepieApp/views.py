from django.shortcuts import render,redirect
from recepieApp.models import Recepie
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url='login/')
def recepie(request):
    recepies=Recepie.objects.all()
    if request.method == 'POST':
        data=request.POST
        recepieName=data.get('recepie-name')
        recepieDescription=data.get('recepie-description')
        recepieImage=data.get('recepie-image')
        print(recepieName,recepieDescription)
        Recepie.objects.create(recepieName=recepieName,recepieDescription=recepieDescription,recepieImage=recepieImage)
        print(recepies)
        return redirect('/')
    print(recepies)
    return render(request,'recepie.html',{'type':'Add','recepies':recepies})
def delete(request,id):
    recepie=Recepie.objects.get(id=id)
    recepie.delete()
    return redirect('/')
def update(request,id):
    recepie=Recepie.objects.get(id=id)
    recepies=Recepie.objects.all()
    if request.method == 'POST':
        data=request.POST
        recepie.recepieName=data.get('recepie-name')
        recepie.recepieDescription=data.get('recepie-description')
        recepie.recepieImage=data.get('recepie-image')
        recepie.save()
        return redirect('/')
    return render(request,'recepie.html',{'type':'Update','recepie':recepie,'recepies':recepies,'url':'update/'+str(id)})
def loginPage(request):
    if request.method=='POST':
        data=request.POST
        userName=data.get('user-name')
        password=data.get('password')
        print(userName,password)
        user=authenticate(username=userName,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials!!!")            
    return render(request,'login.html')
def logoutUser(request):
    logout(request)
    return redirect('/login/')
def registerPage(request):
    if request.method=='POST':
        data=request.POST
        userName=data.get('user-name')
        email=data.get('email')
        password=data.get('password')
        print(userName,password,email)
        if User.objects.filter(username=userName).exists():
            messages.error(request, "Username already exist!!!")            
            return redirect('/register')
        else:
            user=User.objects.create_user(username=userName,password=password,email=email)
            login(request,user)
            return redirect('/')
    return render(request,'register.html')