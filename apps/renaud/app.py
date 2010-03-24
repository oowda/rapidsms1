#!usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

import rapidsms
from rapidsms.parsers.keyworder import Keyworder

class App(rapidsms.app.App):

    keyword = Keyworder()

    def handle(self, message):

        try:
            func, captures = self.keyword.match(self, message.text)
        except TypeError:
            #message.respond(u"Unrecognised message")
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

    keyword.prefix = ['renaud']
    @keyword(r'(\w+) ([y|n])')
    def renaud(self, message, text, exist):
        if exist == 'y':
        	message.respond(u"Hello %s. exist" % text)
	else:
		message.respond(u"Hello %s. does not exist" % text)
	return True
    
    keyword.prefix = ['product']
    @keyword(r'([0-9]+) ([0-9]+)')
    def product(self,message, num , num1 ):
    	    	
    	result = int(num) * int(num1)
    	message.respond(u"the product is %s. " % result)
    	return True
    	