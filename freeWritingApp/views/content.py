from django.shortcuts import render, redirect
from django.contrib import messages
from userApp.models import *
from coreApp.utils import *


def myWritings(request):
    if'user_id' not in request.session:
        messages.error(request, "You need to be logged in to view this page")
        return redirect('/logReg/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        role = request.session['role']
        theUser = user.firstName
        request.session['site'] = 'writing'
        site = request.session['site']
        release = marquee()
        title = {
            'title': 'Free Writing',
            'header': f'Your Free Writing {theUser}'
        }
        context = {
            'user': user,
            'title': title,
            'site': site,
            'role': role,
            'release': release,
        }
        return render(request, 'myWritings.html', context)