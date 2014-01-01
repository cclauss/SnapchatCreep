from googlevoice import Voice
import time
from googlevoice.util import input

voice = Voice()
voice.login()

for x in xrange(0,10):
	for y in xrange(0,10):
		 voice.send_sms("5555512%s%s" % (`x`,`y`), "Add your message here") 
		 time.sleep(10)