from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver








class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=30, blank=True,editable=True)
    start_date = models.DateField(null=True, blank=True)
    ftid = models.TextField(blank=True, max_length=50)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Activity(models.Model):
    PHYSICAL = 'PH'
    SPIRITUAL = 'SP'
    FINANCIAL = 'FI'
    OCCUPATIONAL = 'OC'
    PERSONAL = 'PE'
    NA = 'NA'
    GROUP_CHOICES = [
        (PHYSICAL, 'Physical'),
        (SPIRITUAL, 'Spiritual'),
        (FINANCIAL, 'Financial'),
        (OCCUPATIONAL, 'Occupational'),
        (PERSONAL, 'Personal'),
        (NA, 'NA'),
    ]
    DAY = 'DAY'
    MONTH = 'MTH'
    YEAR = 'YER'
    DUNNO = 'IDK'
    FREQ_CHOICES = [
        (DAY, 'Day'),
        (MONTH, 'Month'),
        (YEAR, 'Year'),
        (DUNNO, 'Choose')
    ]
    name = models.TextField(max_length=100, blank=True)
    details = models.TextField(max_length=200, blank=True,null=True)
    group = models.CharField(max_length= 2, choices= GROUP_CHOICES, default= NA)
    max_complete = models.SmallIntegerField()
    value = models.IntegerField()
    max_points = models.IntegerField()
    frequency = models.SmallIntegerField()
    time_freq = models.CharField(max_length= 3, choices= FREQ_CHOICES, default= DUNNO)

    def __str__(self):
        return self.name + ", Group: " + self.group + ", Max Completions: " + self.max_complete.__str__() + ", Value: " + self.value.__str__()


class CompletedActivity(models.Model):
    comment = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return "" + self.user.user.username + ", " + self.activity.name + ", " + self.date.__str__()


class Reminders(models.Model):
    name = models.TextField(max_length=100, blank=True)
    text = models.TextField(max_length=500, blank=True)
    start = models.DateField(blank=True)
    end = models.DateField(blank=True)
    interval = models.IntegerField()
    check = models.BooleanField()

    def __str__(self):
        return self.name