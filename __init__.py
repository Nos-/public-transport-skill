from mycroft import MycroftSkill, intent_file_handler


class PublicTransport(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('transport.public.intent')
    def handle_transport_public(self, message):
        self.speak_dialog('transport.public')


def create_skill():
    return PublicTransport()

