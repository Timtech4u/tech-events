from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


class Profile(models.Model):
    """
    Profile Model for User 
    Auto Created for each new User
    Registered User can be Organizer or Attendee
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20,  null=True, blank=True)

    def __str__(self):
        return self.user.username

class Interest(models.Model):
    """
    Interests for User-Profile ang Groups
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Group(models.Model):
    """ 
    e.g. DSCBUK
    """
    name = models.CharField(max_length=50)
    leads = models.ForeignKey(Profile, on_delete=models.SET_NULL,  null=True, blank=True)
    interests = models.ForeignKey(Interest, on_delete=models.SET_NULL, null=True, blank=True)
    website = models.URLField(null=True, blank=True, )
    location = models.CharField(max_length=20)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos', null=True, blank=True)
    banner = models.ImageField(upload_to='banners', null=True, blank=True)
    date_created = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        This is done so we can have only one group
        Other groups exist as seperate tenants
        """
        if Group.objects.exists() and not self.pk:
            raise ValidationError("You can only have this group")
        return super(Group, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Event(models.Model):
    """
    This is the model for events in a group.
    """
    title = models.CharField(max_length=50)
    interests = models.ForeignKey(Interest, on_delete=models.SET_NULL, null=True, blank=True)
    organizers = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='organizers')
    # Fetch Attendees Profile from UI and Pass here
    attendees = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='attendees')
    start_date = models.DateTimeField(null=True, blank=True)
    stop_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
