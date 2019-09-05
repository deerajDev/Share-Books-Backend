from django.contrib.auth import get_user_model
from django.db import models

from .helpers import branchChoices, imageUpload, yearChoice

User = get_user_model()


class Book(models.Model):
    owner = models.ForeignKey(
        User, related_name='books', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to=imageUpload)
    book_name = models.CharField(max_length=30, blank=False, null=False)
    author = models.CharField(max_length=50, blank=True, null=True)
    branch = models.CharField(choices=branchChoices(),
                              max_length=40, blank=False, null=False)
    semester = models.PositiveIntegerField(
        choices=yearChoice(), blank=False, null=False, default=1)
    cost = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return self.book_name
