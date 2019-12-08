from django.db import models


# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=16, unique=True, db_column='name')
    s_age = models.IntegerField(default=18, db_column='age')

    class Meta:
        db_table = 'Student'
