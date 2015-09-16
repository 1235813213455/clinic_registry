from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.second_name \
               + " " + self.father_name

class Assignment(models.Model):
    HOUR_1 = {"id":9, "range":"9:00 - 10:00"} 
    HOUR_2 = {"id":10, "range":"10:00 - 11:00"} 
    HOUR_3 = {"id":11, "range":"11:00 - 12:00"}
    HOUR_4 = {"id":12, "range":"12:00 - 13:00"}
    HOUR_5 = {"id":13, "range":"13:00 - 14:00"}
    HOUR_6 = {"id":14, "range":"14:00 - 15:00"}
    HOUR_7 = {"id":15, "range":"15:00 - 16:00"}
    HOUR_8 = {"id":16, "range":"16:00 - 17:00"}
    HOUR_9 = {"id":17, "range":"17:00 - 18:00"}

    HOUR_CHOICES = (HOUR_1, HOUR_2, HOUR_3, HOUR_4, HOUR_5,
                    HOUR_6, HOUR_7, HOUR_8, HOUR_9)

    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    time = models.IntegerField(default=HOUR_1["id"])
    date = models.DateField()

    def __str__(self):
        return "%s: %s (%s, %s)" % (self.doctor, self.patient, date, time)
