from django import forms
from .models import Subject


def validateName(name):
    if not all(x.isalpha for x in name):
        return False
    if not all(x.islower for x in name[1::]):
        return False
    return name[0].isupper()


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"
        firstname = forms.IntegerField(validators=[validateName])
        lastname = forms.IntegerField(validators=[validateName])
