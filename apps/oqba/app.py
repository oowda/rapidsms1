#!/usr/bin/env python
#vim: ai ts=4 sts=4 et sw=4 coding=utf-8
# maintainer: oowda

import rapidsms

class App(rapidsms.app.App):

       def handle(self, message):
		
                if not message.text.startswith('oqba'):
                    return False

                message.respond(u" hello maaaaaaan ")
                return True


                
                