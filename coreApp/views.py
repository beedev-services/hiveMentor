from django.shortcuts import render, redirect
from django.contrib import messages
from userApp.models import *
from coreApp.models import *

# title = {
#     'title': 'Index',
#     'header': 'Hive Mentor',
# }

def index(request):
    title = {
        'title': 'Index',
        'header': 'Hive Mentor',
    }
    request.session['site'] = 'null'
    site = request.session['site']
    request.session['role'] = 'null'
    role = request.session['role']
    if 'user_id' not in request.session:
        user = False
        context = {
            'title': title,
            'user': user,
            'site': site,
            'role': role,
        }
    else:
        user = User.objects.get(id=request.session['user_id'])
        request.session['role'] = user.role
        role = request.session['role']
        context = {
                'user': user,
                'title': title,
                'site': site,
                'role': role,
            }
    return render(request, 'index.html', context)

def about(request):
    title = {
        'title': 'About',
        'header': 'About Hive Mentor'
    }
    site = request.session['site']
    role = request.session['role']
    if 'user_id' not in request.session:
        user = False
        context = {
            'title': title,
            'user': user,
            'site': site,
            'role': role,
        }
    else:
        user = User.objects.get(id=request.session['user_id'])
        request.session['role'] = user.role
        role = request.session['role']
        context = {
                'user': user,
                'title': title,
                'site': site,
                'role': role,
            }
    return render(request, 'about.html', context)

def contact(request):
    title = {
        'title': 'Contact',
        'header': 'Contact - Hive Mentor'
    }
    site = request.session['site']
    role = request.session['role']
    if 'user_id' not in request.session:
        user = False
        context = {
            'title': title,
            'user': user,
            'site': site,
            'role': role,
        }
    else:
        user = User.objects.get(id=request.session['user_id'])
        request.session['role'] = user.role
        role = request.session['role']
        context = {
                'user': user,
                'title': title,
                'site': site,
                'role': role,
            }
    return render(request, 'contact.html', context)

def devNotes(request):
    title = {
        'title': 'Developer Notes',
        'header': 'Hive Mentor',
    }
    request.session['site'] = 'null'
    site = request.session['site']
    request.session['role'] = 'null'
    role = request.session['role']
    versions = Version.objects.values().all()
    features = Feature.objects.values().all()
    statuses = Live.objects.values().all()
    print('versions', versions, 'features', features, 'statuses', statuses)
    if 'user_id' not in request.session:
        user = False
        
        context = {
            'title': title,
            'user': user,
            'site': site,
            'role': role,
            'versions': versions,
            'features': features,
            'statuses': statuses,
        }
    else:
        user = User.objects.get(id=request.session['user_id'])
        request.session['role'] = user.role
        role = request.session['role']
        context = {
                'user': user,
                'title': title,
                'site': site,
                'role': role,
                'versions': versions,
                'features': features,
                'statuses': statuses,
            }
    return render(request, 'devNotes.html', context)

def logReg(request):
    title = {
        'title': 'Login & Registration',
        'header': 'Sign in To Hive Mentor or Create an account'
    }
    site = request.session['site']
    role = request.session['role']
    if 'user_id' not in request.session:
        user = False
        context = {
            'title':title,
            'user': user,
            'site': site,
            'role': role,
        }
        return render(request, 'logReg.html', context)
    else:
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