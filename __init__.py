from mycroft import MycroftSkill, intent_file_handler


class PublicTransport(MycroftSkill):
	def __init__(self):
		MycroftSkill.__init__(self)

	@intent_file_handler('transport.public.intent')
	def handle_transport_public(self, message):
		startort_type = message.data.get('StartOrt')
		zielort_type = message.data.get('ZielOrt')
		linie_type = message.data.get('Linie')
		if zielort_type is not None:
			self.speak_dialog('transport.public',
							{'StartOrt': startort_type, 'ZielOrt': zielort_type})
		else:
			self.speak_dialog('transport.public.generic')

def create_skill():
	return PublicTransport()
	
