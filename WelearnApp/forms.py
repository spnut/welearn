from django import forms

class ProfileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    filePic = forms.ImageField()

class TopicForm(forms.Form):
    post_text = forms.CharField()
    detail = forms.CharField()    

class CommentForm(forms.Form):
    cm = forms.CharField()