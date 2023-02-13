from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # VERY IMPORTANT CHANGE WE SHOULD DO! -> to be able to make/add/make changes later in the process 
    # cellphone_number = models.CharField(max_length=15)
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #1 user to one agent -> one to one field
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE) # if the user profile is deleted, all agents will be deleted as well
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


def post_user_created_signal(sender, instance, created, **kwargs):
    # call this function when recieving the post_signal event 
    # created -> true if user is created only
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)

# once user model is created, django will send post signal, and that funct will 
# handle the event
post_save.connect(post_user_created_signal, sender=User)