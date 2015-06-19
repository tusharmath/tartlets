import datetime
class TimeServer:
    uri = 'com.timeserver.now'
    def execute(self):
        return datetime.datetime.now()