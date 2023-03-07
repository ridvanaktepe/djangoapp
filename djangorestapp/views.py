from django.shortcuts import redirect, render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from djangorestapp.models import Uav, Users
from djangorestapp.serializers import UsersSerializer, UavSerializer
from djangorestapp.forms import UavForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    uav = Uav.objects.all()
    return render(request, "show.html", {'uavs': uav})


def signUp(request):
    if request.method == "POST":
        username = request.POST.get('UserName')
        usermail = request.POST.get('UserMail')
        userpass1 = request.POST.get('UserPassword1')
        userpass2 = request.POST.get('UserPassword2')

        if userpass1 != userpass2:
            return redirect('signup')
        else:
            myuser = User.objects.create_user(username, usermail, userpass1)
            myuser.save()
        return redirect('login')

    return render(request, 'signup.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('UserName')
        userpass = request.POST.get('UserPassword')
        user = authenticate(request, username=username, password=userpass)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'login.html')


def logoutpage(request):
    logout(request)
    return redirect('login')


def addUav(request):
    if request.method == "POST":
        form = UavForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')
            except:
                pass
    else:
        form = UavForm()
    return render(request, 'index.html', {'form': form})


def deleteUav(request, id):
    uav = Uav.objects.get(UavId=id)
    uav.delete()
    return redirect("index")


def editUav(request, id):
    uav = Uav.objects.get(UavId=id)
    return render(request, 'edit.html', {'uav': uav})


def updateUav(request, id):
    uav = Uav.objects.get(UavId=id)
    form = UavForm(request.POST, instance=uav)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, 'edit.html', {'uav': uav})
