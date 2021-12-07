from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile


# @receiver(post_save, sender=Profile)


def createProfile(sender, instance, created, **kwargs):
    if created: # is model record created, then true 
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
        )




def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.save()


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(createProfile, sender=User)    # whenever user is created, profile model is automatically updated
post_save.connect(updateUser, sender=Profile)    # whenever profile is updated, user model is automatically updated
post_delete.connect(deleteUser, sender=Profile)  # whenever profile is deleted, user model is automatically deleted
