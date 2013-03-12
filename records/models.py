from django.db import models
import constants

class Record(models.Model):
    user = models.CharField(max_length=40)
    posted = models.DateTimeField(auto_now_add=True)

class Measurement(models.Model):
    record = models.ForeignKey(Record)
    value = models.FloatField()
    time_measured = models.DateTimeField()
    measurement_type = models.CharField(max_length=15)

    class Meta:
        abstract=True


class WeightMeasurement(Measurement):
    def __init__(self, weight):
        self.measurement_type = "Weight"
        self.value = weight

class BodyFatMeasurement(Measurement):
    def __init__(self, percent):
        self.measurement_type = "BodyFat"
        if percent <= 1 and percent >= 0:
            self.value = percent

        elif percent <= 100 and percent >= 0:
            self.value = percent / 100

        else:
            self = None

class BodySizeMeasurement(Measurement):
    body_part = models.CharField(max_length=6, choices=constants.PARTS)

    def __init__(self, size, metric):
        self.measurement_type = "BodySize"
        if metric == 'inch':
            self.value = size

        elif metric == 'centimeter':
            self.value = size / 2.54

        else:
            self = None

class MaxLiftMeasurement(Measurement):
    lift = models.CharField(max_length=8, choices=constants.LIFTS)

    def __init__(self, reps):
        self.measurement_type = "MaxLift"
        self.value = reps

class RestingHRMeasurement(Measurement):
    def __init__(self, bpm):
        self.measurement_type = "RestingHR"
        self.value = bpm

class SleepMeasurement(Measurement):
    quality = models.FloatField()

    def __init__(self, hrs):
        self.measurement_type = "Sleep"
        self.value = hrs
    

class MugShot(models.Model):
    picture = models.ImageField(upload_to='%M%D%Y/%h%m')
    time_measured = models.DateTimeField()
