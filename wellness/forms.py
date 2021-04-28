import datetime

from django.utils import timezone
from wellness.models import CompletedActivity, Activity, Profile
from django import forms


class PostActivity(forms.Form):
    def __init__(self ,theUser, theActivity, *args, **kwargs):
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
            self.fields[date] = forms.DateTimeField(help_text="Enter a date between now.")
            comment = 'Posting_Comment_%s' % (i + 1,)
            self.fields[comment] = forms.CharField(help_text="Like and Subscribe and leave a comment right here.")





    def clean_date(self):
        data = self.cleaned_data['date']
        date = datetime.datetime.now()
        date2 = datetime.datetime(data.year, data.month, data.day, 0, 0, 0, 0, date.tzinfo)
        data = date2
        return data

    class EditActivity(forms.Form):
        date = forms.DateField(help_text="Enter a date between now.")
        comment = forms.CharField(help_text="Like and Subscribe and leave a comment right here.")

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
        i = 0
        comment_field_name = f'comment_{i}'
        date_field_name = f'comment_{i}'
        while self.cleaned_data.get(comment_field_name):
            comment = self.cleaned_data[comment_field_name]
            if comment in postings:
                self.add_error(comment_field_name, 'Duplicate')
            else:
                postings.append(comment)
            i += 1
            comment_field_name = f'comment_{i}'
        while self.cleaned_data.get(date_field_name):
            date = self.clean_date()
            if date in postings:
                self.add_error(comment_field_name, 'Duplicate')
            else:
                postings.append(date)
            i += 1
            date_field_name = f'date_{i}'
        self.cleaned_data['postings'] = postings

    def save(self, theUser, theActivity):
        posting = self.instance
        posting.date = self.cleaned_data["date"]
        posting.comment = self.cleaned_data["comment"]

        posting.postings_set.all(user=theUser,activity=theActivity).delete()
        for posting in self.cleaned_data['postings']:
            CompletedActivity.objects.create(
                activity=theActivity,
                user=theUser,
                date=self.cleaned_data['postings'].date,
                comment=self.cleaned_data['postings'].comment
            )

