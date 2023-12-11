from django.shortcuts import render, redirect
from django.contrib import messages
from userApp.models import *
from logApp.models import *
from coreApp.utils import *
from chatApp.models import *


def chatAdmin(request):
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
        chatIds = Chat.objects.values().all()
        chatMembers = ChatMembers.objects.values().all()
        release= marquee()
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
            'release': release,
            'chatIds': chatIds,
            'chatMembers': chatMembers,
        }
        return render(request, 'chatAdminDash.html', context)

def sendUsers(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view')
        return redirect('/logReg/')
    user = User.objects.get(id=request.session['user_id'])
    if user.level < 8:
        messages.error(request, 'You do not have permissions to view this page')
    else:
        sendCurrentUsersToChat()
        return redirect('/chat/theAdmin/')
    
def sendUsersGroup(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view')
        return redirect('/logReg/')
    user = User.objects.get(id=request.session['user_id'])
    if user.level < 8:
        messages.error(request, 'You do not have permissions to view this page')
    else:
        theGroup_id = request.POST['chatID']
        chatAdmin = request.POST['chatAdmin']
        sendCurrentUsersToGroup(theGroup_id, chatAdmin)
        return redirect('/chat/theAdmin/')
    
def getUsersChat(request):
    getUsersInChat()
    return redirect('/chat/theAdmin/')

def checkUser(request):
    getAdminAcct()
    return redirect('/chat/theAdmin/')

def getGroupUsers(request):
    theGroup_id = request.POST['chatID']
    chatAdmin = request.POST['chatAdmin']
    getCurrentUsersInGroup(theGroup_id, chatAdmin)
    return redirect('/chat/theAdmin/')