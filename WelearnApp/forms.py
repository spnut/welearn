from django import forms

class ProfileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    filePic = forms.ImageField()