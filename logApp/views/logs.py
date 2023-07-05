from django.shortcuts import render, redirect
from django.contrib import messages
from userApp.models import *
from logApp.models import *
from django.core.paginator import Paginator

# title = {
#     'title': 'Index',
#     'header': 'Hive Mentor',
# }
# context = {
#     'title': title,
# }

def logDash(request):
    title = {
        'title': 'Log Dashboard',
        'header': 'Hive Mentor - Log Dashboard',
    }
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in to view your logs')
        return redirect('/logReg/')
    user = User.objects.get(id=request.session['user_id'])
    theWeeks = Week.objects.filter(user_id=request.session['user_id']).order_by('-createdAt')
    paginator = Paginator(theWeeks, 5)
    pageNum = request.GET.get('page')
    weeks = paginator.get_page(pageNum)
    days = Day.objects.filter(author_id=request.session['user_id'])
    request.session['site'] = 'logs'
    request.session['role'] = user.role
    role = request.session['role']
    site = request.session['site']
    context = {
        'title': title,
        'user': user,
        'site': site,
        'weeks': weeks,
        'days': days,
        'role': role,
    }
    return render(request, 'logDash.html', context)


# ***** Week functions *****
def createWeek(request):
    newWeek = Week.objects.create(
        title=request.POST['title'],
        user=User.objects.get(id=request.session['user_id']),
    )
    newWeek = newWeek.id
    messages.error(request, 'Week Created')
    return redirect(f'/logs/week/{newWeek}/')

def viewWeek(request, week_id):
    week = Week.objects.get(id=week_id)
    days = Day.objects.filter(week_id=week_id)
    print(days)
    if not days:
        days = False
    print('final days', days)
    weekTitle = week.title
    title = {
        'title':weekTitle,
        'header': f'Hive Mentor - {weekTitle}'
    }
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in to view page')
        return redirect('/logReg/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        request.session['role'] = user.role
        role = request.session['role']
        site = request.session['site']
        context = {
            'title': title,
            'week': week,
            'user': user,
            'site': site,
            'days': days,
            'role': role,
        }
        return render(request, 'viewWeek.html', context)
    
def editWeek(request, week_id):
    pass

def updateWeek(request, week_id):
    pass

def deleteWeek(request, week_id):
    pass

# ***** Day Functions *****
def createDay(request, week_id):
    newDay = Day.objects.create(
        day = request.POST['day'],
        week_id = week_id,
        author = User.objects.get(id=request.session['user_id'])
    )
    newDay = newDay.id
    messages.error(request, 'Day Created')
    return redirect(f'/logs/week/{week_id}/day/{newDay}/')

def viewDay(request, week_id, day_id):
    week = Week.objects.get(id=week_id)
    day = Day.objects.get(id=day_id)
    weekTitle = week.title
    dayTitle = day.day
    title = {
        'title': f'{dayTitle} of {weekTitle}',
        'header': f'Hive Mentor - {dayTitle} of {weekTitle}'
    }
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in to view page')
        return redirect('/logReg/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        journal = Journal.objects.filter(journal_id=day_id)
        request.session['role'] = user.role
        role = request.session['role']
        print(journal)
        if not journal:
            journal = False
        site = request.session['site']
        context = {
            'title': title,
            'week': week,
            'user': user,
            'site': site,
            'day': day,
            'journal': journal,
            'role': role,
        }
        return render(request, 'viewDay.html', context)

def deleteDay(request, day_id):
    pass

# ***** List Functions *****
def addSymptom(request):
    pass

def createSymptom(request):
    pass

def addMedication(request):
    pass

def createNewMed(request):
    pass

# ******* Optional Functions *******

# ***** Journal Functions *****
def createJournal(request, week_id, day_id):
    Journal.objects.create(
        title = request.POST['title'],
        content = request.POST['content'],
        journal_id = day_id,
        writer = User.objects.get(id=request.session['user_id'])
    )
    messages.error(request, 'Journal Entry Created')
    return redirect(f'/logs/week/{week_id}/day/{day_id}/')

def viewJournal(request, journal_id):
    pass

def editJournal(request, journal_id):
    pass

def updateJournal(request, journal_id):
    pass

def deleteJournal(request, journal_id):
    pass

# ***** Mood Functions *****
def newMood(request):
    pass

def createMood(request):
    pass

def deleteMood(request, mood_id):
    pass

# ***** Sleep Functions *****
def newSleep(request):
    pass

def createSleep(request):
    pass

def deleteSleep(request, sleep_id):
    pass

# ***** Food Functions *****
def newFood(request):
    pass

def createFood(request):
    pass

def deleteFood(request, food_id):
    pass


# ***** Med Functions *****
def newMed(request):
    pass

def createMed(request):
    pass

def deleteMed(request, medication_id):
    pass

# ***** Diabetic Functions *****
def newSugar(request):
    pass

def createSugar(request):
    pass

def deleteSugar(request, sugar_id):
    pass