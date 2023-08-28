from django.shortcuts import render, redirect
from django.contrib import messages
from userApp.models import *
from coreApp.models import *
from userApp.util import *
from coreApp.apiUtil import *

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
    release = marquee()
    # print('release data', release)
    if 'user_id' not in request.session:
        user = False
        context = {
            'title': title,
            'user': user,
            'site': site,
            'role': role,
            'release': release,
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
                'release':release
            }
    return render(request, 'index.html', context)

def theProj(request):
    versions = Version.objects.all().values()
    features = Feature.objects.all().values()
    status = Live.objects.all().values()
    production = []
    dev = []
    local = []
    back = []
    for s in status:
        stat = {}
        if(s['live'] == 'Production'):
            if(s['dateOfRelease']):
                stat['date'] = s['dateOfRelease']
            else:
                stat['date'] = 'TBD'
            stat['version'] = []
            for v in versions:
                vers = {}
                if(v['id'] == s['liveVersion_id']):
                    vers['num'] = v['versionNum']
                    vers['info'] = v['info']
                    stat['version'].append(vers)
            stat['feature'] = []
            for f in features:
                feat = {}
                if(f['id'] == s['liveFeature_id']):
                    feat['name'] = f['name']
                    feat['info'] = f['info']
                    stat['feature'].append(feat)
            production.append(stat)
        if(s['live'] == 'Development'):
            if(s['dateOfRelease']):
                stat['date'] = s['dateOfRelease']
            else:
                stat['date'] = 'TBD'
            stat['version'] = []
            for v in versions:
                vers = {}
                if(v['id'] == s['liveVersion_id']):
                    vers['num'] = v['versionNum']
                    vers['info'] = v['info']
                    stat['version'].append(vers)
            stat['feature'] = []
            for f in features:
                feat = {}
                if(f['id'] == s['liveFeature_id']):
                    feat['name'] = f['name']
                    feat['info'] = f['info']
                    stat['feature'].append(feat)
            dev.append(stat)
        if(s['live'] == 'Local'):
            if(s['dateOfRelease']):
                stat['date'] = s['dateOfRelease']
            else:
                stat['date'] = 'TBD'
            stat['version'] = []
            for v in versions:
                vers = {}
                if(v['id'] == s['liveVersion_id']):
                    vers['num'] = v['versionNum']
                    vers['info'] = v['info']
                    stat['version'].append(vers)
            stat['feature'] = []
            for f in features:
                feat = {}
                if(f['id'] == s['liveFeature_id']):
                    feat['name'] = f['name']
                    feat['info'] = f['info']
                    stat['feature'].append(feat)
            local.append(stat)
        if(s['live'] == 'BackLog'):
            if(s['dateOfRelease']):
                stat['date'] = s['dateOfRelease']
            else:
                stat['date'] = 'TBD'
            stat['version'] = []
            for v in versions:
                vers = {}
                if(v['id'] == s['liveVersion_id']):
                    vers['num'] = v['versionNum']
                    vers['info'] = v['info']
                    stat['version'].append(vers)
            stat['feature'] = []
            for f in features:
                feat = {}
                if(f['id'] == s['liveFeature_id']):
                    feat['name'] = f['name']
                    feat['info'] = f['info']
                    stat['feature'].append(feat)
            back.append(stat)
    data = {
        'production': production,
        'dev': dev,
        'local': local,
        'back': back,
    }
    return render(request, 'theboard.html', data)

def about(request):
    title = {
        'title': 'About',
        'header': 'About Hive Mentor'
    }
    site = request.session['site']
    role = request.session['role']
    release = marquee()
    if 'user_id' not in request.session:
        user = False
        context = {
            'title': title,
            'user': user,
            'site': site,
            'role': role,
            'release': release,
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
                'release': release,
            }
    return render(request, 'about.html', context)

def contact(request):
    title = {
        'title': 'Contact',
        'header': 'Contact - Hive Mentor'
    }
    site = request.session['site']
    role = request.session['role']
    release = marquee()
    if 'user_id' not in request.session:
        user = False
        context = {
            'title': title,
            'user': user,
            'site': site,
            'role': role,
            'release': release,
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
                'release': release,
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
    updates = Release.objects.values().all()
    release = marquee()
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
            'release': release,
            'updates': updates,
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
                'release': release,
                'updates': updates,
            }
    return render(request, 'devNotes.html', context)

def logReg(request):
    title = {
        'title': 'Login & Registration',
        'header': 'Sign in To Hive Mentor or Create an account'
    }
    site = request.session['site']
    role = request.session['role']
    release = marquee()
    if 'user_id' not in request.session:
        user = False
        context = {
            'title':title,
            'user': user,
            'site': site,
            'role': role,
            'release': release
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
        release = marquee()
        title = {
            'title': 'Chose Site',
            'header': '',
        }
        context = {
            'user': user,
            'title': title,
            'site': site,
            'role': role,
            'release': release
        }
        return render(request, 'choseRole.html', context)