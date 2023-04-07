from django.db import models

class contact(models.Model):
    Name = models.CharField(max_length=30, null=False),
    email = models.EmailField(max_length=45, primary_key=True, null=True),
    Team_Contact = models.IntegerField(max_length=20, default=92),
    comment = models.CharField(max_length=300, null=True),
    contact_start = models.DateTimeField(auto_now_add=True),