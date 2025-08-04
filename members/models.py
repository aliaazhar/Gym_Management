from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)
    membership_plan = models.CharField(max_length=100)

    def __str__(self):
        return self.name
