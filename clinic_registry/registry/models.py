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
        return self.second_name + " " + self.first_name \
               + " " + self.father_name

class Assignment(models.Model):
    HOUR_MAP = {9: {"id":9, "range":"9:00 - 10:00"}, 
                10: {"id":10, "range":"10:00 - 11:00"}, 
                11: {"id":11, "range":"11:00 - 12:00"},
                12: {"id":12, "range":"12:00 - 13:00"},
                13: {"id":13, "range":"13:00 - 14:00"},
                14: {"id":14, "range":"14:00 - 15:00"},
                15: {"id":15, "range":"15:00 - 16:00"},
                16: {"id":16, "range":"16:00 - 17:00"},
                17: {"id":17, "range":"17:00 - 18:00"}}
    HOUR_CHOICES = HOUR_MAP.values()

    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    time = models.IntegerField(default=HOUR_MAP[9]["id"], 
                               choices=[(k, v["range"]) for k, v in HOUR_MAP.items()])
    date = models.DateField()


    def time_string(self):
        return Assignment.HOUR_MAP[self.time]["range"] 

    time_string.short_description = "Time"


    def __str__(self):
        assignment_time = Assignment.HOUR_MAP[self.time]
        return "%s: %s (%s, %s)" % (self.doctor, self.patient, str(self.date), assignment_time["range"])
