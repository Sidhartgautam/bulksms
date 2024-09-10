from django import forms

from django import forms

class EmailUploadForm(forms.Form):
    csv_file = forms.FileField()
