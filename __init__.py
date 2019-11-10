from mycroft import MycroftSkill, intent_file_handler, intent_handler
# from adapt.intent import IntentBuilder


class PublicTransport(MycroftSkill):
	def __init__(self):
		MycroftSkill.__init__(self)

#	def initialize(self):
#		self.register_intent_file('transport.public.intent', self.handle_transport.public)

	@intent_file_handler('nach.transport.public.intent')
	def handle_transport_public(self, message):
		startort_type = message.data.get('StartOrt')
		zielort_type = message.data.get('ZielOrt')
		linie_type = message.data.get('Linie')

		print ("zielOrt:")
		print ( type(zielort_type) )
		print ( zielort_type )
		if zielort_type is not None:
			self.speak_dialog('transport.public',
#							{'StartOrt': startort_type, 'ZielOrt': zielort_type})
							{'ZielOrt': zielort_type})
#           self.speak("Well, I'm not sure if I like " + tomato_type + " tomatoes.")
		else:
			self.speak_dialog('transport.public.generic')

def create_skill():
	return PublicTransport()
	
