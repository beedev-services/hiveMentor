from django.db import models
from django.db.models.deletion import CASCADE
from userApp.models import User

# ***** List Models *****

class SymptomList(models.Model):
    symptom = models.CharField(max_length=255)
    info = models.TextField(blank=True)

    def __str__(self):
        return self.symptom

class MedList(models.Model):
    name = models.CharField(max_length=255)
    freq = models.CharField(max_length=255, default='daily')
    
    def __str__(self):
        return self.name
    def fullMed(self):
        return f'{self.name} {self.freq}'
    
class FitnessList(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class FoodList(models.Model):
    category = models.CharField(max_length=255, default='Meat')
    food = models.CharField(max_length=255)
    calories = models.CharField(max_length=255, default=0)
    def __str__(self):
        return self.food
    def fullFood(self):
        return f'{self.food} {self.calories}'

# ***** Default Required Models *****

class Week(models.Model):
    title = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='theUser', on_delete=CASCADE)

    def __str__(self):
        return self.title

class Day(models.Model):
    day = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    week = models.ForeignKey(Week, related_name='theWeek', on_delete=CASCADE)
    author = models.ForeignKey(User, related_name='theAuthor', on_delete=CASCADE)

    def __str__(self):
        return f'{self.day} {self.date}'
    
class Mood(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    feeling = models.IntegerField(blank=True)
    symptom = models.ForeignKey(SymptomList, related_name='theSymptom',on_delete=CASCADE)
    comments = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    log = models.ForeignKey(Day, related_name='theLog',on_delete=CASCADE, blank=True)
    feeler = models.ForeignKey(User, related_name='theFeeler', on_delete=CASCADE)

    def __str__(self):
        return f'{self.feeler.username} - {self.date}'

class Water(models.Model):
    water = models.IntegerField(default=0)
    comments = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    note = models.ForeignKey(Day, related_name='theNote', on_delete=CASCADE)
    drinker = models.ForeignKey(User, related_name='theDrinker', on_delete=CASCADE)

    def __str__(self):
        return f'{self.drinker.username} - {self.water}'

# ***** Default Optional Models *****

class Journal(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    journal = models.ForeignKey(Day, related_name='theJournal',on_delete=CASCADE, blank=True)
    writer = models.ForeignKey(User, related_name='theWriter', on_delete=CASCADE)

    def __str__(self):
        return f'{self.writer.username} - {self.title} {self.journal.date}'

class Sleep(models.Model):
    date = models.DateField()
    sleep = models.TimeField()
    wake = models.TimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    night = models.ForeignKey(Day, related_name='theNight', on_delete=CASCADE)
    sleeper = models.ForeignKey(User, related_name='theSleeper', on_delete=CASCADE)
    def __str__(self):
        return f'{self.sleeper.username} - {self.date}'

class Food(models.Model):
    meal = models.CharField(max_length=255, blank=True)
    servings = models.IntegerField(default=1)
    comments = models.TextField(blank=True)
    totalCals = models.IntegerField(default=0)
    foodCat = models.CharField(max_length=255, default='Meats')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    foodItem = models.ForeignKey(FoodList, related_name='theFoodItem', on_delete=CASCADE)
    record = models.ForeignKey(Day, related_name='theRecord', on_delete=CASCADE)
    person = models.ForeignKey(User, related_name='thePerson', on_delete=CASCADE)
    def __str__(self):
        return f'{self.person.username} - {self.meal} {self.totalCals}'

class Medication(models.Model):
    when = models.DateTimeField()
    dose = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    medication = models.ForeignKey(MedList, related_name='theMed', on_delete=CASCADE)
    blog = models.ForeignKey(Day, related_name='theBlog',on_delete=CASCADE, blank=True)
    member = models.ForeignKey(User, related_name='theMember', on_delete=CASCADE)
    def __str__(self):
        return f'{self.member.username} - {self.when}'

class Sugar(models.Model):
    time = models.TimeField()
    level = models.IntegerField()
    testSite = models.CharField(max_length=255, default='Finger Stick')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    entry = models.ForeignKey(Day, related_name='theEntry',on_delete=CASCADE, blank=True)
    owner = models.ForeignKey(User, related_name='theOwner', on_delete=CASCADE)
    def __str__(self):
        return f'{self.owner.username} - {self.time}'

class Weight(models.Model):
    weight = models.IntegerField()
    unit = models.CharField(max_length=255, default='LBS')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    day = models.ForeignKey(Day, related_name='theDay',on_delete=CASCADE)
    userWeight = models.ForeignKey(User, related_name='theUserWeight', on_delete=CASCADE)
    def __str__(self):
        return f'{self.userWeight.username} - {self.day.date}'

class Fitness(models.Model):
    duration = models.CharField(max_length=255, default="30")
    unit = models.CharField(max_length=255, default="min")
    comments = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    exercise = models.ForeignKey(FitnessList, related_name='theExercise', on_delete=CASCADE)
    workout = models.ForeignKey(Day, related_name='theWorkout', on_delete=CASCADE)
    human = models.ForeignKey(User, related_name='theHuman', on_delete=CASCADE)
    def __str__(self):
        return f'{self.human.username} - {self.exercise.name}'

class Work(models.Model):
    duration = models.CharField(max_length=255, default="4")
    comments = models.TextField(blank=True)
    job = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    workDay = models.ForeignKey(Day, related_name='theWorkDay', on_delete=CASCADE)
    worker = models.ForeignKey(User, related_name='theWorker', on_delete=CASCADE)
    def __str__(self):
        return f'{self.worker.username} - {self.duration}'

class Weather(models.Model):
    temp = models.CharField(max_length=255)
    pressure = models.CharField(max_length=255)
    humidity = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    conditions = models.ForeignKey(Day, related_name='theConditions', on_delete=CASCADE)
    userWeather = models.ForeignKey(User, related_name='theUserWeather', on_delete=CASCADE)
    def __str__(self):
        return f'{self.userWeather.username} - {self.pressure}'