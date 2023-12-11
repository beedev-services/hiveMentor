import requests
import json
from coreApp.models import *
from coreApp.config import *
import string
import random

weatherAPI = WEATHER_KEY

def marquee():
    current = Release.objects.get(releaseType='Current')
    minor = Release.objects.get(releaseType='Minor')
    major = Release.objects.get(releaseType='Major')
    initial = Release.objects.get(releaseType='Initial')
    releaseInfo = []
    if not minor:
        minor = False
    else:
        releaseMinor = {
        'id': 3,
        'date': minor.date,
        'version': minor.version,
        'type': minor.releaseType,
        }
    releaseInfo.append(releaseMinor)
    if not major:
        major = False
    else:
        releaseMajor = {
        'id': 4,
        'date': major.date,
        'version': major.version,
        'type': major.releaseType,
        }
    releaseInfo.append(releaseMajor)
    if not initial:
        initial = False
    else:
        releaseInitial = {
        'id': 1,
        'date': initial.date,
        'version': initial.version,
        'type': initial.releaseType,
        }
    releaseInfo.append(releaseInitial)
    if not current:
        current = False
    else:
        releaseCurrent = {
        'id': 2,
        'date': current.date,
        'version': current.version,
        'type': current.releaseType,
        }
    releaseInfo.append(releaseCurrent)
    # print('release data', releaseInfo[0]['timeSinceInitial'])
    if releaseInfo[0] == False:
        return False
    return releaseInfo

def projBoard():
    versions = list(Version.objects.all().values())
    features = list(Feature.objects.all().values())
    status = list(Live.objects.all().values())
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
    return data



def latLong(theZip):
    geoUrl = f"http://api.openweathermap.org/geo/1.0/zip?zip={theZip}{weatherAPI}"
    response = requests.get(geoUrl)
    res = response.json()
    return res

def getConditions(lat, lon):
    weatherUrl = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&units=imperial{weatherAPI}"
    response = requests.get(weatherUrl)
    res = response.json()
    return res

def convertToMins(hrs, mins):
    time = 0
    if not hrs:
        theHrs = 0
    if not mins:
        theMins = 0
    if mins:
        theMins = int(mins)
    if hrs:
        temp = int(hrs)
        if temp > 1:
            theHrs = temp*60
        if temp == 1:
            theHrs = int(60)
    time = int(theHrs) + int(theMins)
    return time

def randomCodeGenerator():
    N = 12
    res = ''.join(random.choices(string.ascii_letters, k=N))
    theCode = str(res)
    return theCode
