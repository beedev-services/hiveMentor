from coreApp.models import *
import string
import random

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


def randomCodeGenerator():
    N = 12
    res = ''.join(random.choices(string.ascii_letters, k=N))
    theCode = str(res)
    return theCode