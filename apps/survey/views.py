#!usr/bin/env python
# encoding=utf-8
# maintainer: oowda

from django.http import HttpResponse
from rapidsms.webui.utils import render_to_response

from models import Survey
from models import Activities
from django.contrib.auth.decorators import login_required

import math 

def index (request):
    '''return HttpResponse("Hello world !")'''
    

    result = Survey.objects.all()
    male = Survey.objects.filter(sex='M')
    female = Survey.objects.filter(sex='F')
    
    malePercent = int(float(male.count()) / (result.count()) * 100)
    femalePercent = int(float(female.count()) / ( result.count()) *100)

    actSt = Activities.objects.filter(code='1')
    actProf = Activities.objects.filter(code='2')
    
    activiteySt = Survey.objects.filter(activity=actSt)
    activiteyProf = Survey.objects.filter(activity=actProf)

    activiteyStPercent = int(float(activiteySt.count()) / (result.count()) * 100) 
    activiteyProfPercent = int(float(activiteyProf.count()) / (result.count()) * 100) 
    

    return render_to_response(request,'survey/template.html',{'allrecords':result,'profrerecords':activiteyProfPercent,'strerecords':activiteyStPercent,'malerecords':malePercent,'femalerecords':femalePercent})
@login_required
def profile(request, userid):
    profile = Survey.objects.get(id=userid) 
    return render_to_response(request,'survey/profile.html',{'profile':profile})