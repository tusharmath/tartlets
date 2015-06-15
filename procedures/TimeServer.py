from autobahn.asyncio.wamp import ApplicationSession
from autobahn.asyncio.wamp import ApplicationRunner


class TimeServer(ApplicationSession):
    def onJoin(self, details):
        def now(x):
            return x

        self.register(now, 'com.timeserver.now')


runner = ApplicationRunner(url=u"ws://localhost:8080/ws", realm=u"realm1")
runner.run(TimeServer)