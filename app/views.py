from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User

import json

from .models import SkillSet, UserDetail
from .forms import ApplicationForm


class UserApplication(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = ApplicationForm(request.POST)

        if form.is_valid():
            # Create User for authentication.
            user_obj, created = User.objects.get_or_create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'])
            # Create skill.
            skill_set = set(i.strip().lower()
                            for i in form.cleaned_data['skills'].split(','))
            skill_obj = set()
            for skill in skill_set:
                obj, created = SkillSet.objects.get_or_create(name=skill)
                skill_obj.add(obj)
            obj, created = UserDetail.objects.get_or_create(
                user=user_obj,
                gender=form.cleaned_data['gender'],
                qualification=form.cleaned_data['qualification'],
                passing_year=form.cleaned_data['passing_year'],
                company=form.cleaned_data['company'],
                ctc=form.cleaned_data['ctc'],
                experience=form.cleaned_data['experience'],
                percentage=form.cleaned_data['percentage']
            )
            if created:
                for i in skill_obj:
                    obj.skills.add(i)
            return HttpResponse(
                '''<center><b>Thanks for registration, HR Team will contact you
                 soon.</b></center>''')
        else:
            error_fields = dict(json.loads(form.errors.as_json())).keys()
            return render(request, self.template_name,
                          {'errors': error_fields})
