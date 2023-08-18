from django.shortcuts import render, redirect
from django.contrib import messages
from userApp.models import *
from logApp.models import *
import string
import random
from userApp.util import *

def theAdmin(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view')
        return redirect('/logReg/')
    user = User.objects.get(id=request.session['user_id'])
    if user.level < 6:
        messages.error(request, 'You do not have permissions to view this page')
    else:
        role = request.session['role']
        request.session['site'] = 'admin'
        site = request.session['site']
        users = User.objects.values().all()
        weeks = Week.objects.values().all()
        days = Day.objects.values().all()
        counts = {
            'users': users.count,
            'weeks': weeks.count,
            'days': days.count,
        }
        title = {
            'title': 'Admin',
            'header': 'Admin'
        }
        context = {
            'user': user,
            'title': title,
            'site': site,
            'role': role,
            'users': users,
            'weeks': weeks,
            'days': days,
            'counts': counts,
        }
        return render(request, 'theAdmin.html', context)

def sendUsers(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view')
        return redirect('/logReg/')
    user = User.objects.get(id=request.session['user_id'])
    if user.level < 8:
        messages.error(request, 'You do not have permissions to view this page')
    else:
        sendCurrentUsersToChat()
        return redirect('/user/theAdmin/')
    
def getUsersChat(request):
    getUsersInChat()
    return redirect('/user/theAdmin/')

def checkUser(request):
    getAdminAcct()
    return redirect('/user/theAdmin/')

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
    return redirect('/user/theAdmin/theCodes/')