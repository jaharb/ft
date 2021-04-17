import datetime
from django.utils import timezone

from django import forms


class PostActivity(forms.Form):
    date = forms.DateField(help_text="Enter a date between now.")
    comment = forms.CharField(help_text="Like and Subscribe and leave a comment right here.")

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