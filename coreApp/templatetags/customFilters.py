from django import template
from datetime import datetime, timedelta

register = template.Library()


@register.filter(name='hoursSlept')
def hoursSlept(sleep):
    sleepDate = sleep.date
    startTime = sleep.sleep
    endTime = sleep.wake
    sleepStart = datetime.combine(sleepDate, startTime)
    sleepEnd = datetime.combine(sleepDate, endTime)
    if sleepEnd < sleepStart:
        sleepEnd += timedelta(days=1)
    timeSlept = (sleepEnd - sleepStart).total_seconds() / 3600
    return round(timeSlept, 2)

@register.filter(name='updateDate')
def updateDate(sleep):
    sleepDate = sleep.date
    startTime = sleep.sleep
    endTime = sleep.wake
    sleepStart = datetime.combine(sleepDate, startTime)
    sleepEnd = datetime.combine(sleepDate, endTime)
    if sleepEnd < sleepStart:
        # Sleep spans across two dates, so return the end date
        sleepEnd += timedelta(days=1)
        formatedDate = sleepEnd.strftime("%b. %d, %Y")
    return formatedDate


@register.filter(name='convertToHoursMins')
def convertToHoursMins(job):
    time = job.duration
    hours, minutes = divmod(time, 60)
    return hours, minutes
