from django.shortcuts import render, redirect
from django.contrib import messages
from userApp.models import *
from logApp.models import *
import bcrypt
<<<<<<< HEAD
from coreApp.utils import *
=======
from userApp.util import *
from coreApp.apiUtil import *
>>>>>>> bdd0cb018e9f1d27605f74d73b069a3840555638

def login(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            if userLogin.id == 1:
                messages.error(request, f'Welcome back Admin {userLogin.firstName}')
            request.session['role'] = userLogin.role
            # sendSignupEmail(userLogin)
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
    sendSignupEmail(newUser)
    # sendUserToChat(newUser.username, newUser.email, newUser.firstName, newUser.lastName,newUser.role)
    return redirect('/choseRole/')

def forgotPassword(request):
    title = {
        'title': 'ForgotPassword',
        'header': 'ForgotPassword'
        }
    release = marquee()
    site = request.session['site']
    role = request.session['role']
    if 'user_id' not in request.session:
        user = False
    context = {
        'title':title,
        'user': user,
        'site': site,
        'role': role,
        'release': release
    }
    return render(request, 'forgotPassword.html', context)

def requestPassCode(request):
    if request.POST['username']:
        theUser = User.objects.filter(username = request.POST['username'])
        if theUser:
            user = theUser[0]
        else:
            messages.error(request, 'Username not our system')
            return redirect('/user/forgotpassword/')
    elif request.POST['email']:
        theUser = User.objects.filter(email = request.POST['email'])
        if theUser:
            user = theUser[0]
        else:
            messages.error(request, 'Email not in our system')
            return redirect('/user/forgotpassword/')
    else:
        messages.error(request, 'Please enter your email or username')
        return redirect('/user/forgotpassword/')
    theCode = randomCodeGenerator()
    PassCode.objects.create(
        code = theCode,
        requester = User.objects.get(id=user.id)
    )
    forgotPasswordEmail(user, theCode)
    return redirect('/logReg/')

def passwordReset(request):
    title = {
        'title': 'Reset Password',
        'header': 'Reset Password'
        }
    release = marquee()
    site = request.session['site']
    role = request.session['role']
    if 'user_id' not in request.session:
        user = False
    context = {
        'title':title,
        'user': user,
        'site': site,
        'role': role,
        'release': release
    }
    return render(request, 'resetPassword.html', context)

def resetPass(request):
    if request.POST['username']:
        theUser = User.objects.filter(username = request.POST['username'])
        if theUser:
            user = theUser[0]
        else:
            messages.error(request, 'Username not our system')
            return redirect('/user/password-reset/')
    elif request.POST['email']:
        theUser = User.objects.filter(email = request.POST['email'])
        if theUser:
            user = theUser[0]
        else:
            messages.error(request, 'Email not in our system')
            return redirect('/user/password-reset/')
    else:
        messages.error(request, 'Please enter your email or username')
        return redirect('/user/password-reset/')
    theCode = PassCode.objects.get(code=request.POST['resetCode'])
    if theCode:
        print('the code', theCode)
        if theCode.requester_id != user.id:
            messages.error(request, 'Invalid reset Code')
            return redirect('/user/password-reset/')
    else:
        messages.error(request, 'Invalid reset Code')
        return redirect('/user/password-reset/')
    if len(request.POST['password']) < 6:
        messages.error(request, 'Password must be at least 6 characters long')
        return redirect('/user/password-reset/')
    if request.POST['password'] != request.POST['confirm']:
        messages.error(request, 'Passwords do not match')
        return redirect('/user/password-reset/')
    else:
        hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        toUpdate = User.objects.get(id=user.id)
        toUpdate.password = hashedPw
        toUpdate.save()
        alsoUpdate = PassCode.objects.get(code=request.POST['resetCode'])
        alsoUpdate.used=1
        alsoUpdate.save()
        request.session['user_id'] = user.id
        messages.error(request, f'Password updated, welcome back, {user.firstName}')
        return redirect('/choseRole/')
