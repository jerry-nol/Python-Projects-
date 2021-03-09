from django.db import models
from django.core.validators import MaxValueValidator


# My model
class djangoClasses(models.Model):
    title = models.CharField(max_length=20)
    course_number = models.IntegerField(null=False, default='', blank=True,validators=[MaxValueValidator(999)])
    instructor = models.CharField(null=False, default='', blank=True, max_length=60)
    duration = models.DurationField()

    objects = models.Manager()

    def __str__(self):
        #returning the title attribute
        return self.title #