from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # VERY IMPORTANT CHANGE WE SHOULD DO! -> to be able to make/add/make changes later in the process 
    # cellphone_number = models.CharField(max_length=15)
    pass

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #1 user to one agent -> one to one field

    def __str__(self):
        return self.user.email


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    # Foreign key field -> relationships between models
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE) #if "Agent" -> means Agent is inside the file (otherwise order matters)
    # on_delete => if agent is deleted, do: 
    # - models.CASCADE → delete a lead
    # - models.SETNULL +null=True → set it to NULL
    # - models.SET_DEFAULT + default=… → set it to a default

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

