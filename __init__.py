from mycroft import MycroftSkill, intent_file_handler
import os
import time


class Stop(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('stop.intent')
    def handle_stop(self, message):
        self.speak_dialog('stop')
        time.sleep(10)
        os.system('shutdown -P now')


def create_skill():
    return Stop()

