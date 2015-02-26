import googlevoice
import time
#from googlevoice.util import input

voice = googlevoice.Voice()
voice.login()

for x in xrange(10):
	for y in xrange(10):
		 voice.send_sms("5555512%s%s" % (`x`,`y`), "Add your message here") 
		 time.sleep(10) #so Google won't rate limit
