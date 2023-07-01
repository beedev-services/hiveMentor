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
    user = User.objects.filter(id=request.session['user_id'])
    theWeeks = Week.objects.filter(user_id=request.session['user_id']).order_by('-createdAt')
    paginator = Paginator(theWeeks, 5)
    pageNum = request.GET.get('page')
    weeks = paginator.get_page(pageNum)
    days = Day.objects.filter(author_id=request.session['user_id'])
    print(weeks)
    print('the user', user[0])
    request.session['site'] = 'logs'
    site = request.session['site']
    context = {
        'title': title,
        'user': user[0],
        'site': site,
        'weeks': weeks,
        'days': days,
    }
    return render(request, 'logDash.html', context)



    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


def newWeek(request):
    title = {
        'title':'Create Week',
        'header': 'Hive Mentor - Create Week'
    }
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in to view page')
        return redirect('/logReg/')
    user = User.objects.filter(id=request.session['user_id'])
    site = request.session['site']
    context = {
        'title': title,
        'user': user[0],
        'site': site
    }
    return render(request, 'createWeek.html', context)

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
        site = request.session['site']
        context = {
            'title': title,
            'week': week,
            'user': user,
            'site': site,
            'days': days,
        }
        return render(request, 'viewWeek.html', context)