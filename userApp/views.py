from django.shortcuts import render, redirect
from django.contrib import messages
from userApp.models import *
import bcrypt
import string
import random
import datetime


def index(request):
    title = {
        'title': 'Index',
        'header': 'Hive Mentor',
    }
    request.session['site'] = 'null'
    site = request.session['site']
    if 'user_id' not in request.session:
        user = False
        context = {
            'title': title,
            'user': user,
            'site': site,
        }
    else:
        user = User.objects.get(id=request.session['user_id'])
        user = user
        context = {
                'user': user,
                'title': title,
                'site': site
            }
    return render(request, 'index.html', context)

def about(request):
    title = {
        'title': 'About',
        'header': 'About Hive Mentor'
    }
    request.session['site'] = 'null'
    site = request.session['site']
    if 'user_id' not in request.session:
        user = False
        context = {
            'title': title,
            'user': user,
            'site': site
        }
    else:
        user = User.objects.get(id=request.session['user_id'])
        user = user
        context = {
                'user': user,
                'title': title,
                'site': site
            }
    return render(request, 'about.html', context)

def contact(request):
    title = {
        'title': 'Contact',
        'header': 'Contact - Hive Mentor'
    }
    request.session['site'] = 'null'
    site = request.session['site']
    if 'user_id' not in request.session:
        user = False
        context = {
            'title': title,
            'user': user,
            'site': site
        }
    else:
        user = User.objects.get(id=request.session['user_id'])
        user = user
        context = {
                'user': user,
                'title': title,
                'site': site
            }
    return render(request, 'contact.html', context)

def logReg(request):
    title = {
        'title': 'Login & Registration',
        'header': 'Sign in To Hive Mentor or Create an account'
    }
    request.session['site'] = 'null'
    site = request.session['site']
    if 'user_id' not in request.session:
        user = False
        context = {
            'title':title,
            'user': user,
            'site': site
        }
        return render(request, 'logReg.html', context)
    else:
        return redirect('/choseRole/')

def login(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            if userLogin.id == 1:
                messages.error(request, f'Welcome back Admin {userLogin.firstName}')
            request.session['role'] = userLogin.role
            return redirect('/choseRole/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/logReg/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    return redirect('/logReg/')

def reg(request):
    if request.method == 'GET':
        return redirect('/logReg/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/logReg/')
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
        toUpdate = User.objects.get(id=request.session['user_id'])
        toUpdate.level=10
        toUpdate.role = 'Webmaster'
        toUpdate.save()
    messages.error(request, f'Welcome {newUser.firstName}')
    request.session['role'] = newUser.role
    return redirect('/choseRole/')

def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/')

def choseRole(request):
    if 'user_id' not in request.session:
        return redirect('/logReg/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        request.session['role'] = user.role
        role = request.session['role']
        site = request.session['site']
        title = {
            'title': 'Chose Site',
            'header': '',
        }
        context = {
            'user': user,
            'title': title,
            'site': site,
            'role': role,
        }
        return render(request, 'choseRole.html', context)

def profile(request):
    if 'user_id' not in request.session:
        messages.error(request, "you need to be logged in to view this page")
        return redirect('/logReg/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        request.session['role'] = user.role
        role = request.session['role']
        theUser = user.firstName
        request.session['site'] = 'profile'
        site = request.session['site']
        title = {
            'title': 'Profile',
            'header': f'Your information {theUser}'
        }
        context = {
            'user': user,
            'title': title,
            'site': site,
            'role': role,
        }
        return render(request, 'profile.html', context)
    
def updateDiabetic(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.diabetic=request.POST['diabetic']
    toUpdate.save()
    messages.error(request, 'Updated Diabetic Question')
    return redirect('/profile/')

def updateFood(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.food=request.POST['food']
    toUpdate.save()
    messages.error(request, 'Updated Food Question')
    return redirect('/profile/')

def updateSleep(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.sleep=request.POST['sleep']
    toUpdate.save()
    messages.error(request, 'Updated Sleep Question')
    return redirect('/profile/')

def updateMood(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.mood=request.POST['mood']
    toUpdate.save()
    messages.error(request, 'Updated Mood Question')
    return redirect('/profile/')

def updateMeds(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.meds=request.POST['meds']
    toUpdate.save()
    messages.error(request, 'Updated Medication Question')
    return redirect('/profile/')

def updateJournal(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.journal=request.POST['journal']
    toUpdate.save()
    messages.error(request, 'Updated Journal Question')
    return redirect('/profile/')

def theAdmin(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view')
        return redirect('/logReg/')
    user = User.objects.get(id=request.session['user_id'])
    if user.level < 6:
        messages.error(request, 'You do not have permissions to view this page')
    else:
        request.session['role'] = user.role
        role = request.session['role']
        request.session['site'] = 'admin'
        site = request.session['site']
        title = {
            'title': 'Admin',
            'header': 'Admin'
        }
        context = {
            'user': user,
            'title': title,
            'site': site,
            'role': role,
        }
        return render(request, 'theAdmin.html', context)

def theCodes(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view')
        return redirect('/logReg/')
    user = User.objects.get(id=request.session['user_id'])
    if user.level < 6:
        messages.error(request, 'You do not have permissions to view this page')
    else:
        codes = Code.objects.values().all()
        N = 12
        res = ''.join(random.choices(string.ascii_letters, k=N))
        theCode = str(res)
        role = request.session['role']
        request.session['site'] = 'admin'
        site = request.session['site']
        title = {
            'title': 'Codes',
            'header': 'Upgrading Codes'
        }
        context = {
            'user': user,
            'title': title,
            'site': site,
            'role': role,
            'theCode': theCode,
            'codes': codes,
        }
        return render(request, 'theCodes.html', context)

def createCode(request):
    Code.objects.create(
        code = request.POST['code'],
        role = request.POST['role'],
        creator = User.objects.get(id=request.session['user_id'])
    )
    messages.error(request, 'New Code Generated')
    return redirect('/theAdmin/theCodes/')

def upgradeAccount(request):
    theCode = request.POST['code']
    codeCheck = Code.objects.filter(code = theCode).values()
    if codeCheck:
        newRole = codeCheck[0]['role']
        newUse = codeCheck[0]['used']
        codeId = codeCheck[0]['id']
        ifCode = Code.objects.get(id=codeId)
        print('codeCheck', codeCheck, 'codeId',codeId, 'ifCode', ifCode, 'sessionUser', User.objects.get(id=request.session['user_id']))
        toUpdate=Code.objects.get(id=codeId)
        toUpdate.used = newUse+1
        toUpdate.save()
        if newRole == 'Trainer':
            newLevel = 2
        if newRole == 'Mentor':
            newLevel = 4
        if newRole == 'Provider':
            newLevel = 4
        if newRole == 'ChatAdmin':
            newLevel = 6
        if newRole == 'SuperAdmin':
            newLevel = 8
        if newRole == 'Webmaster':
            newLevel = 10
        toUpdate=User.objects.get(id=request.session['user_id'])
        toUpdate.role = newRole
        toUpdate.level = newLevel
        toUpdate.save()
        messages.error(request, f'Your account has been updated to {newRole}')
    else:
        messages.error(request, 'The code you entered is not correct')
    return redirect('/profile/')