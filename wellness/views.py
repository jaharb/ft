from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.db.models import Sum
from django.urls import reverse
import datetime
from wellness.forms import PostActivity
from django.http import HttpResponseRedirect
from wellness.models import Activity, CompletedActivity, Profile

def index(request):
    """View function for home page of site."""
    home_user = Profile.objects.get(pk=1)
    num_activities = Activity.objects.count()
    Cactivity = CompletedActivity.objects.filter(user=home_user)
    UActivity = Cactivity.values('activity_id', 'activity__name', 'activity__value', 'activity__group').annotate \
    (count=Count('activity__name'), earned=Sum('activity__value'))
    TimesCompelted = Cactivity.annotate(count=Count('activity__name'))
    # Generate counts of some of the main objects








    context = {
        'huser': home_user,
        'Lname' : home_user.user.last_name,
        'Fname': home_user.user.first_name,
        'num_activities': num_activities,
        'activity_list' : UActivity,
        "times_completed" : TimesCompelted
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
def post(request):
    """View function for post page of site."""
    home_user = Profile.objects.get(pk=1)
    num_activities = Activity.objects.count()
    AllActivites = Activity.objects.all()


    # Generate counts of some of the main objects








    context = {
        'huser': home_user,
        'Lname' : home_user.user.last_name,
        'Fname': home_user.user.first_name,
        'allactivites': AllActivites,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'post.html', context=context)

def postact(request, pk):
    home_user = Profile.objects.get(pk=1)
    activity = Activity.objects.get(pk=pk)
    if request.method == 'POST':

        form = PostActivity(request.POST)
        if form.is_valid():
            new = CompletedActivity(activity=activity, user=home_user, comment=form.cleaned_data['comment'], \
                                    date=form.cleaned_data['date'])
            new.save()
            return HttpResponseRedirect(reverse('post'))
    else:
        from datetime import timezone

        form = PostActivity(initial={'date': "", 'comment': ""})

    context = {
        'huser': home_user,
        'Lname': home_user.user.last_name,
        'Fname': home_user.user.first_name,
        'form': form,
        'activity': activity,
    }
    return render(request, 'postact.html', context=context)

def editpost(request, user_id, act_id):
    home_user = Profile.objects.get(pk=1)
    activity = CompletedActivity.objects.get(user=home_user, activity=act_id)
    if request.method == 'POST':

        form = PostActivity(request.POST)
        if form.is_valid():
            activity.comment = form.comment
            activity.date = form.date

            return HttpResponseRedirect(reverse('index'))
    else:
        from datetime import timezone

        form = PostActivity(initial={'date': "", 'comment': ""})

    context = {
        'huser': home_user,
        'Lname': home_user.user.last_name,
        'Fname': home_user.user.first_name,
        'form': form,
        'activity': activity,
    }
    return render(request, 'postact.html', context=context)