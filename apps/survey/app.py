#!usr/bin/env python
# encoding=utf-8
# maintainer: oowda

import rapidsms
from rapidsms.parsers.keyworder import Keyworder
from models import Survey
from models import Activities
import time
from datetime import date


class App(rapidsms.app.App):

    keyword = Keyworder()

    def handle(self, message):

        try:
            func, captures = self.keyword.match(self, message.text)
        except TypeError:
            message.respond(u"Unrecognised message")
            return False
        try:
            return func(self, message, *captures)
        except Exception, e:
            message.respond(u"System encountered an Error: %s" % e)
            return True

    def old_handle(self, message):
        ''' not used anymore '''
        if message.text.lower().startswith('renaud'):
            message.respond(u"Hello %s" % message.text)
            return True

        return False

    keyword.prefix = ['help']
    @keyword(r'')
    def renaud(self, message):
        
       	message.respond(u"Enter the word 'survey' follwed by: firstName lastName gender(M:male,F:female) age activity(1:student, 2:professional) - To serch for enter St for student search or Prof for professionals ")
	return True
    
    keyword.prefix = ['survey']
    @keyword(r'([a-z]+) ([a-z]+) ([M|F]) ([0-9]+) ([1|2])')
    def survey(self,message, fname , lname, gender ,age, activity ):
    	
    	if gender == 'M':
        	sex = 'Male'
	else:
		sex = 'Female'
	
	if activity == '1':
	        prof = 'Student'
	else:
		prof = 'Professional'
    	
    	act = Activities.objects.get(code=activity)
    	survey = Survey(firsName=fname , lastName=lname, sex=gender, age=age, activity=act, enteredDate = date.today() )
    	
    	try:
    		survey.save()
    		message.respond(u"You have entered  first name :%s. last name: %s. gender: %s. age: %s. activity: %s. " %((fname,lname,sex,age,prof)))
    	except:
    		message.respond(u"Faild to insert")
	return True 
	
    keyword.prefix = ['search']
    @keyword(r'([a-z]+)')
    def search(self,message, act):

    	if act.lower() == 'st':
		serchCrit = '1'
	else:
		serchCrit = '2'
	activ = Activities.objects.get(code=serchCrit)
	result = Survey.objects.filter(activity=activ)
	
	persons_a = []        
	for person in result:
		persons_a.append(person.lastName)
	answer = u"%s People. " % result.__len__()        
	answer += u", ".join(persons_a)         
	message.respond(answer[:160])
		
	return True 
	
    ''' @keyword('')
    def stats(self, message):
    returns the number of records in DB.
    	persons = Person.objects.all()       
    	message.respond(u"Survey database knows about %d persons." \   % persons.__len__())
    	return True'''
	