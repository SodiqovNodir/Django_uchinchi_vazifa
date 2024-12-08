from django.db import models
from django.db.models import DateTimeField, ImageField, CASCADE


class Course(models.Model):
    title = models.CharField(max_length=150)
    description =  models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    enrolled_at = DateTimeField()
    photo = models.ImageField(upload_to="students/photos/", blank=True, null=True)
    course =models.ForeignKey(Course, on_delete=CASCADE)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name