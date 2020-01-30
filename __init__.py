from mycroft import MycroftSkill, intent_file_handler


class Stop(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('stop.intent')
    def handle_stop(self, message):
        self.speak_dialog('stop')


def create_skill():
    return Stop()

