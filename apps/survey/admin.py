#!/usr/bin/env python
#vim ai ts=4 sts=4 et sw=4

from django.contrib import admin	
from models import Survey
from models import Activities

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('firsName', 'lastName','sex','age','activity','enteredDate')
	list_filter = ('sex','activity')
	ordirenig = [('enteredDate')]
	search_fields = ['firsName', 'lastName','age','sex']
	
admin.site.register(Survey, ProfileAdmin)
admin.site.register(Activities)

