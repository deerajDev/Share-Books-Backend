from django.db import models
from django.contrib.auth import get_user_model
from .helpers import branchChoices , yearChoice , imageUpload

User =  get_user_model()



class Book(models.Model):
    owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=imageUpload)
    book_name = models.CharField(max_length=30, blank=False, null=False)
    author = models.CharField(max_length=50,blank=True, null=True)
    branch = models.CharField(choices=branchChoices(),max_length=40, blank=False, null=False)
    semester = models.PositiveIntegerField(choices=yearChoice(), max_length=20,blank=False, null=False,default=1)
    cost =models.PositiveIntegerField(blank=False, null=False)
    
    def __str__(self):
        return self.book_name