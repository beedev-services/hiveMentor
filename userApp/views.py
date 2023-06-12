from django.shortcuts import render, redirect
from django.contrib import messages
from userApp.models import *
import bcrypt


def index(request):
    title = {
        'title': 'Index',
        'header': 'Hive Mentor',
    }
    context = {
        'title': title,
    }
    return render(request, 'temp.html', context)

def about(request):
    title = {
        'title': 'About',
        'header': 'About Hive Mentor'
    }
    context = {
        'title':title,
    }
    return render(request, 'about.html', context)

def contact(request):
    title = {
        'title': 'Contact',
        'header': 'Contact - Hive Mentor'
    }
    context = {
        'title':title
    }
    return render(request, 'contact.html', context)

def logReg(request):
    title = {
        'title': 'Login & Registration',
        'header': 'Sign in To Hive Mentor or Create an account'
    }
    if 'user_id' not in request.session:
        context = {
            'title':title
        }
        return render(request, 'logReg.html', context)
    else:
        user = User.objects.filter(id = 'user_id')
        if user.level > 1:
            if 'role' not in request.session:
                return redirect('/choseRole')
            else:
                return redirect('/dashboard')
        else:
            return redirect('/dashboard')

def login(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            if userLogin.level > 1:
                return redirect('/choseRole')
            else:
                return redirect('/dashboard')

def reg(request):
    if request.method == 'GET':
        return redirect('/logReg')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/logReg')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        username = request.POST['username'],
        email = request.POST['email'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    if newUser.id == 1:
        toUpdate = User.objects.get(id=request.session['user_d'])
        toUpdate.level=24
        toUpdate.save()
        messages.error(request, 'Welcome Admin')
        return redirect('/')
    else:
        messages.error(request, 'Welcome')

def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/logReg')
    else:
        user = User.objects.filter(id = 'user_id')
        pass

def choseRole(request):
    if 'user_id' not in request.session:
        return redirect('/logReg')
    else:
        user = User.objects.filter(id = 'user_id')
        pass
