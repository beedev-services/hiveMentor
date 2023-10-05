from django.shortcuts import render, redirect
from django.contrib import messages
from userApp.models import *
from logApp.models import *
from coreApp.utils import *

def profile(request):
    if 'user_id' not in request.session:
        messages.error(request, "you need to be logged in to view this page")
        return redirect('/logReg/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        role = request.session['role']
        theUser = user.firstName
        request.session['site'] = 'profile'
        site = request.session['site']
        release = marquee()
        title = {
            'title': 'Profile',
            'header': f'Your information {theUser}'
        }
        context = {
            'user': user,
            'title': title,
            'site': site,
            'role': role,
            'release': release,
        }
        return render(request, 'profile.html', context)
    
def updateDiabetic(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.diabetic=request.POST['diabetic']
    toUpdate.save()
    messages.error(request, 'Updated Diabetic Question')
    return redirect('/user/profile/')

def updateFood(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.food=request.POST['food']
    toUpdate.save()
    messages.error(request, 'Updated Food Question')
    return redirect('/user/profile/')

def updateSleep(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.sleep=request.POST['sleep']
    toUpdate.save()
    messages.error(request, 'Updated Sleep Question')
    return redirect('/user/profile/')

def updateMood(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.mood=request.POST['mood']
    toUpdate.save()
    messages.error(request, 'Updated Mood Question')
    return redirect('/user/profile/')

def updateMeds(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.meds=request.POST['meds']
    toUpdate.save()
    messages.error(request, 'Updated Medication Question')
    return redirect('/user/profile/')

def updateJournal(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.journal=request.POST['journal']
    toUpdate.save()
    messages.error(request, 'Updated Journal Question')
    return redirect('/user/profile/')

def updateFitness(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.fitness=request.POST['fitness']
    toUpdate.save()
    messages.error(request, 'Updated Fitness Question')
    return redirect('/user/profile/')

def updateWork(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.work=request.POST['work']
    toUpdate.save()
    messages.error(request, 'Updated Work Question')
    return redirect('/user/profile/')

def updateWeather(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.weather=request.POST['weather']
    toUpdate.save()
    messages.error(request, 'Updated Weather Question')
    return redirect('/user/profile/')

def updateWeight(request):
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.weight=request.POST['weight']
    toUpdate.save()
    messages.error(request, 'Updated Weight Question')
    return redirect('/user/profile/')

def addZip(request):
    theZip = request.POST.get('zipCode')
    theData = latLong(theZip)
    toUpdate=User.objects.get(id=request.session['user_id'])
    toUpdate.profile.zipCode=theZip
    toUpdate.profile.lat = theData['lat']
    toUpdate.profile.lon = theData['lon']
    toUpdate.save()
    messages.error(request, 'Updated ZipCode Question')
    return redirect('/user/profile/')


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
    return redirect('/user/profile/')
