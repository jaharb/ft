from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.db.models import Sum
from django.urls import reverse
import datetime
from wellness.forms import PostActivity, EditActivity
from django.http import HttpResponseRedirect, HttpResponse
from wellness.models import Activity, CompletedActivity, Profile

def index(request):
    """View function for home page of site."""
    home_user = Profile.objects.get(pk=1)
    """num_activities = Activity.objects.count()"""
    Cactivity = CompletedActivity.objects.filter(user=home_user)
    UActivity = Cactivity.values('activity_id', 'activity__name', 'activity__value', 'activity__group').annotate \
    (count=Count('activity__name'), earned=Sum('activity__value'))
    TimesCompelted = Cactivity.annotate(count=Count('activity__name'))
    # Generate counts of some of the main objects








    context = {
        'huser': home_user,
        'Lname' : home_user.user.last_name,
        'Fname': home_user.user.first_name,
        'num_activities': 1,
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

def postact(request, act_id):
    home_user = Profile.objects.get(pk=1)
    act = Activity.objects.get(pk=act_id)
    if request.method == 'POST':
        form = PostActivity(home_user, act, request.POST)
        if form.is_valid():
            form.save(home_user, act)
            return HttpResponseRedirect(reverse('post'))
        else:
            return HttpResponse("you failed, big L")
    else:
        from datetime import timezone
        form = PostActivity(home_user, act)
        context = {
            'huser': home_user,
            'Lname': home_user.user.last_name,
            'Fname': home_user.user.first_name,
            'form': form,
            'activity': act,
        }
    return render(request, 'postact.html', context=context)

def editpost(request, act_id):
    home_user = Profile.objects.get(pk=1)
    act = Activity.objects.get(pk=act_id)
    if request.method == 'POST':
        form = EditActivity(home_user, act, request.POST)
        if form.is_valid():
            form.save(home_user, act)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("you failed, big L")
    else:
        from datetime import timezone
        form = EditActivity(home_user, act)
        context = {
            'huser': home_user,
            'Lname': home_user.user.last_name,
            'Fname': home_user.user.first_name,
            'form': form,
            'activity': act,
            }

        return render(request, 'postact.html', context=context)


