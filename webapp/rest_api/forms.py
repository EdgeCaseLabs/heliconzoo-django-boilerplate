from django import forms

class BeginSessionViewForm(forms.Form):
    auth_user_id = forms.CharField()
    session_id = forms.CharField()
