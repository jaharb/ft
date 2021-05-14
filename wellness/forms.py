import datetime

from django.utils import timezone
from wellness.models import CompletedActivity, Activity, Profile
from django import forms


class PostActivity(forms.Form):
    def __init__(self ,theUser, theActivity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        postings_list = CompletedActivity.objects.filter(user=theUser, activity=theActivity)
        max_comp = theActivity.max_complete
        for i in range(max_comp):
            date = 'Posting_Date_%s' % (i + 1,)
            comment = 'Posting_Comment_%s' % (i + 1,)
            try:
                self.initial[date] = postings_list[i].date
            except:
                self.initial[date] = ""
            try:
                self.initial[comment] = postings_list[i].comment
            except:
                self.initial[comment] = ""
            date = 'Posting_Date_%s' % (i + 1,)
            self.fields[date] = forms.DateTimeField(help_text="Enter a Date.", required=False)
            comment = 'Posting_Comment_%s' % (i + 1,)
            self.fields[comment] = forms.CharField(help_text="Enter a comment.", required=False)
        date = forms.DateField(help_text="Enter a date.", required=False)
        comment = forms.CharField(help_text="Enter a comment", required=False)





    def clean_date(self):
        data = self.cleaned_data['date']
        date = datetime.datetime.now()
        date2 = datetime.datetime(data.year, data.month, data.day, 0, 0, 0, 0, date.tzinfo)
        data = date2
        return data


    def clean_comment(self):
        data = self.cleaned_data['comment']
        return data

    def clean(self):
        postings = []
        i = 1
        date_field_name = f'Posting_Date_{i}'
        comment_field_name = f'Posting_Comment_{i}'
        while self.cleaned_data.get(date_field_name):
            cleaned_date = self.cleaned_data[date_field_name]
            cleaned_comment = self.cleaned_data[comment_field_name]
            this_post = PostingData(cleaned_date, cleaned_comment)
            postings.append(this_post)
            i += 1
            date_field_name = f'Posting_Date_{i}'
            comment_field_name = f'Posting_Comment_{i}'
        self.cleaned_data['postings'] = postings

    def save(self, theUser, theActivity):
        CompletedActivity.objects.filter(user=theUser, activity=theActivity).delete()
        for posting in self.cleaned_data['postings']:
            CompletedActivity.objects.create(
                activity=theActivity,
                user=theUser,
                date=posting.date,
                comment=posting.comment
            )


class PostingData:
    def __init__(self, date, comment):
        self.date = date
        self.comment = comment

class EditActivity(forms.Form):
    def __init__(self, theUser, theActivity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        postings_list = CompletedActivity.objects.filter(user=theUser, activity=theActivity)
        for i in range(len(postings_list)):
            date = 'Posting_Date_%s' % (i + 1,)
            comment = 'Posting_Comment_%s' % (i + 1,)
            try:
                self.initial[date] = postings_list[i].date
            except:
                self.initial[date] = ""
            try:
                self.initial[comment] = postings_list[i].comment
            except:
                self.initial[comment] = ""
            date = 'Posting_Date_%s' % (i + 1,)
            self.fields[date] = forms.DateTimeField(help_text="Enter a Date.")
            comment = 'Posting_Comment_%s' % (i + 1,)
            self.fields[comment] = forms.CharField(help_text="Enter a comment.")
        date = forms.DateField(help_text="Enter a date.", required=False)
        comment = forms.CharField(help_text="Enter a comment", required=False)

    def clean_date(self):
        data = self.cleaned_data['date']
        date = datetime.datetime.now()
        date2 = datetime.datetime(data.year, data.month, data.day, 0, 0, 0, 0, date.tzinfo)
        data = date2
        return data

    def clean_comment(self):
        data = self.cleaned_data['comment']
        return data

    def clean(self):
        postings = []
        i = 1
        date_field_name = f'Posting_Date_{i}'
        comment_field_name = f'Posting_Comment_{i}'
        while self.cleaned_data.get(date_field_name):
            cleaned_date = self.cleaned_data[date_field_name]
            cleaned_comment = self.cleaned_data[comment_field_name]
            this_post = PostingData(cleaned_date,cleaned_comment)
            postings.append(this_post)
            i += 1
            date_field_name = f'Posting_Date_{i}'
            comment_field_name = f'Posting_Comment_{i}'
        self.cleaned_data['postings'] = postings

    def save(self, theUser, theActivity):
        CompletedActivity.objects.filter(user=theUser, activity=theActivity).delete()
        for posting in self.cleaned_data['postings']:
            CompletedActivity.objects.create(
                activity=theActivity,
                user=theUser,
                date=posting.date,
                comment=posting.comment
            )
class Filter(forms.Form):
        filter = forms.CharField(max_length=2, choices=Activity.GROUP_CHOICES, default='NA')