from django.db import models
from django.db.models.deletion import CASCADE

class Version(models.Model):
    versionNum = models.CharField(max_length=255)
    info = models.TextField()
    def __str__(self):
        return self.versionNum


class Feature(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    def __str__(self):
        return self.name

class Live(models.Model):
    liveVersion = models.ForeignKey(Version, related_name='theLiveVersion', on_delete=CASCADE)
    liveFeature = models.ForeignKey(Feature, related_name='theLiveFeature', on_delete=CASCADE)
    dateOfRelease = models.DateField(blank=True, null=True)
    live = models.BooleanField(default=0)

class Release(models.Model):
    version = models.CharField(max_length=255)
    releaseType = models.CharField(max_length=255)
    date = models.DateTimeField()
    def __str__(self):
        return f'{self.releaseType} - {self.version} - {self.date}'