


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
