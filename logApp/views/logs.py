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
weekDays = [
    {1: 'Sunday'},
    {2: 'Monday'},
    {3: 'Tuesday'},
    {4: 'Wednesday'},
    {5: 'Thursday'},
    {6: 'Friday'},
    {7: 'Saturday'}
]

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
    if not weeks:
        weeks = False
    days = Day.objects.filter(author_id=request.session['user_id'])
    request.session['site'] = 'logs'
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
        role = request.session['role']
        site = request.session['site']
        context = {
            'title': title,
            'week': week,
            'user': user,
            'site': site,
            'days': days,
            'role': role,
            'weekDays': weekDays,
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
        moods = Mood.objects.filter(log_id=day_id)
        sleeps = Sleep.objects.filter(night_id=day_id)
        foods = Food.objects.filter(record_id=day_id)
        water = Water.objects.filter(note_id=day_id)
        meds = Medication.objects.filter(blog_id=day_id)
        sugars = Sugar.objects.filter(entry_id=day_id)
        sList = SymptomList.objects.values().all()
        mList = MedList.objects.values().all()
        role = request.session['role']
        print(journal)
        print(water)
        if not water:
            water = False
        else:
            water = water[0]
        if not journal:
            journal = False
        else:
            journal = journal[0]
        site = request.session['site']
        context = {
            'title': title,
            'week': week,
            'user': user,
            'site': site,
            'day': day,
            'journal': journal,
            'role': role,
            'moods': moods,
            'sleeps': sleeps,
            'foods': foods,
            'water': water,
            'meds': meds,
            'sugars': sugars,
            'sList': sList,
            'mList': mList,
        }
        # print('the journal', journal.title)
        return render(request, 'viewDay.html', context)

def deleteDay(request, day_id):
    pass

# ***** List Functions *****

def createSymptom(request):
    currPage = request.POST['currPage']
    print('the url being passed in', currPage)
    SymptomList.objects.create(
        symptom = request.POST['symptom'],
        info = request.POST['info']
    )
    messages.error(request, 'Symptom added to Symptom Bank')
    return redirect(f'{currPage}')

def createNewMed(request):
    currPage = request.POST['currPage']
    MedList.objects.create(
        name = request.POST['name'],
        freq = request.POST['freq'],
    )
    messages.error(request, "Medication added to Medication Bank")
    return redirect(f'{currPage}')

def addFitness(request):
    pass

def createNewFitness(request):
    pass

# ******* Default Required Functions *******

# ***** Mood Functions *****
def createMood(request, week_id, day_id):
    Mood.objects.create(
        feeling = request.POST['feeling'],
        symptom_id = request.POST['symptom'],
        comments = request.POST['comments'],
        log_id = day_id,
        feeler = User.objects.get(id=request.session['user_id'])
    )
    messages.error(request, 'Mood Added')
    return redirect(f'/logs/week/{week_id}/day/{day_id}/')

def deleteMood(request, mood_id):
    pass

# ***** Water Functions *****
def createWater(request, week_id, day_id):
    Water.objects.create(
        water = 1,
        note_id = day_id,
        drinker = User.objects.get(id=request.session['user_id'])
    )
    messages.error(request, 'Water logged')
    return redirect(f'/logs/week/{week_id}/day/{day_id}/')

def updateWater(request, week_id, day_id, water_id):
    theWater = Water.objects.filter(note_id=day_id)
    theWater = theWater[0].water
    toUpdate=Water.objects.get(id=water_id)
    toUpdate.water=theWater+1
    toUpdate.save()
    messages.error(request, 'Water logged')
    return redirect(f'/logs/week/{week_id}/day/{day_id}/')

def deleteWater(request):
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
def createMed(request, week_id, day_id):
    Medication.objects.create(
        when = request.POST['when'],
        dose = request.POST['dose'],
        medication_id = request.POST['medication'],
        blog_id = day_id,
        member = User.objects.get(id=request.session['user_id'])
    )
    messages.error(request, 'Medication logged')
    return redirect(f'/logs/week/{week_id}/day/{day_id}/')

def deleteMed(request, medication_id):
    pass

# ***** Diabetic Functions *****
def newSugar(request):
    pass

def createSugar(request):
    pass

def deleteSugar(request, sugar_id):
    pass