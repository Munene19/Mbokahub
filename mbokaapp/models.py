
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()


from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Create your models here.

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
)

CATEGORY = (
    ('Electricity and wiring', "Electricity and wiring"),
    ('Welding', "Welding"),
    ('Plant operator', "Plant operator"),
    ('Plumbing', "Plumbing"),
    ('Construction', "Construction"),
    ('Painting', "Painting"),
    ('Carpentry', "Carpentry"),
    ('Sanitation', "Sanitation"),
    ('Catering', "Catering"),
    ('Gardening', "gardening"),
    ('Farm labor', "Farm labor"),
    ('Minor labor', "Minor labor"),
)

class Category(models.Model):
    name = models.CharField(choices=CATEGORY,  max_length=40)

    def __str__(self):
        return self.name
    

class Job(models.Model):

    user = models.ForeignKey(User, related_name='Use', on_delete=models.CASCADE) 
    title = models.CharField(max_length=300)
    description = RichTextField()
    tags = TaggableManager()
    location = models.CharField(max_length=300)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    category = models.ForeignKey(Category,related_name='Category', on_delete=models.CASCADE)
    salary = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=300)
    company_contact_information = models.CharField(max_length=300, blank=True)
    last_date = models.DateField()
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

 

class Applicant(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title


  

class BookmarkJob(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title