from coreApp.models import *

def marquee():
    current = Release.objects.get(releaseType='Current')
    minor = Release.objects.get(releaseType='Minor')
    major = Release.objects.get(releaseType='Major')
    initial = Release.objects.get(releaseType='Initial')

    releaseInfo = []

    releaseInitial = {
        'id': 1,
        'date': initial.date,
        'version': initial.version,
        'type': initial.releaseType,
    }
    releaseCurrent = {
        'id': 2,
        'date': current.date,
        'version': current.version,
        'type': current.releaseType,
    }
    releaseMinor = {
        'id': 3,
        'date': minor.date,
        'version': minor.version,
        'type': minor.releaseType,
    }
    releaseMajor = {
        'id': 4,
        'date': major.date,
        'version': major.version,
        'type': major.releaseType,
    }
    releaseInfo.append(releaseInitial)
    releaseInfo.append(releaseCurrent)
    releaseInfo.append(releaseMinor)
    releaseInfo.append(releaseMajor)
    # print('release data', releaseInfo[0]['timeSinceInitial'])
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