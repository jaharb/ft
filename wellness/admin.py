from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Profile, Activity, CompletedActivity, Reminders


class AllActsAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'max_complete', 'value', 'max_points')


class CompActsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'comment', 'activity')


admin.site.register(Activity, AllActsAdmin)
admin.site.register(Profile)
admin.site.register(CompletedActivity)
admin.site.register(Reminders)



