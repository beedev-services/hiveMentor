from django.shortcuts import render, redirect
from django.contrib import messages
from userApp.models import *
from logApp.models import *
from userApp.util import *

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
        title = {
            'title': 'Profile',
            'header': f'Your information {theUser}'
        }
        context = {
            'user': user,
            'title': title,
            'site': site,
            'role': role,
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



#     api_url = f"https://api.example.com/geo/{zip_code}"  # Replace with the actual API URL

#     try:
#         # Make the API call to get latitude and longitude
#         response = requests.get(api_url)
#         response_data = response.json()

#         # Check if the API call was successful and contains latitude and longitude
#         if response.status_code == 200 and 'latitude' in response_data and 'longitude' in response_data:
#             latitude = response_data['latitude']
#             longitude = response_data['longitude']

#             # Save the data to the database
#             location = Location.objects.create(zip_code=zip_code, latitude=latitude, longitude=longitude)

#             # Return the saved data in the response
#             return JsonResponse({
#                 'zip_code': location.zip_code,
#                 'latitude': location.latitude,
#                 'longitude': location.longitude
#             })

#         else:
#             # If the API call was not successful or didn't contain latitude and longitude
#             return HttpResponseBadRequest("Invalid API response or zip code not found.")

#     except requests.exceptions.RequestException as e:
#         # If there was an exception during the API call (e.g., network error)
#         return HttpResponseBadRequest(f"Error occurred during API call: {e}")
