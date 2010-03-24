#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 coding=utf-8
# maintainer: oowda

from django.db import models 


class Activities(models.Model) :

    code = models.CharField(max_length=2, unique=True,verbose_name="Occupation code")
    name = models.CharField(max_length=30,verbose_name="Occupation name")

    def __unicode__(self):
	    return u"%s (%s)" % (self.code, self.name)
	    
class Survey( models.Model ):
	
	firsName= models.CharField(max_length=30,verbose_name="Person first name")
	lastName= models.CharField(max_length=30,verbose_name="Person last name")
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
    	)
	sex = models.CharField(max_length=1, choices=GENDER_CHOICES,verbose_name="person gender")
	age= models.DecimalField(max_digits=2, decimal_places=0,verbose_name="person age")
	activity = models.ForeignKey(Activities,help_text="Occupation st,developer ")
	enteredDate = models.DateTimeField()
	
	def __unicode__(self):
	    return u"%s (%s) (%s) (%s) (%s)" % (self.firsName, self.lastName, self.sex, self.age, self.enteredDate)
	
	@property
	def name(self):
		''' returns the full name '''
		return u"%(first)s %(last)s" % {'first': self.firsName.title(), \
						'last': self.lastName.upper()}
	