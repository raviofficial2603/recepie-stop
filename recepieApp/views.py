from django.shortcuts import render,redirect
from recepieApp.models import Recepie
# Create your views here.
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