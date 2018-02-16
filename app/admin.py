from django.contrib import admin
from .models import SkillSet, UserDetail


class UserDetailAdmin(admin.ModelAdmin):
    list_display = ['user', 'experience', 'ctc', 'accepted']
    ordering = ['accepted']


admin.site.register(SkillSet)
admin.site.register(UserDetail, UserDetailAdmin)