from django import forms


class ApplicationForm(forms.Form):
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'Female'),
    )
    QUALIFICATION_CHOICES = (
        ('btech', 'B Tech'),
        ('bsc', 'BSc (IT)'),
        ('mca', 'MCA'),
    )
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    qualification = forms.ChoiceField(choices=QUALIFICATION_CHOICES, widget=forms.RadioSelect())
    passing_year = forms.IntegerField()
    percentage = forms.DecimalField()
    company = forms.CharField()
    ctc = forms.DecimalField()
    experience = forms.IntegerField()
    skills = forms.CharField()