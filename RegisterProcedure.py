from autobahn.asyncio.wamp import ApplicationSession
from autobahn.asyncio.wamp import ApplicationRunner
import datetime

# CONSTANTS
CROSSBAR_REALM = u"async-worker"
CROSSBAR_URL = u"ws://localhost:8080/ws"


# RPC
def com_timeserver_now():
    return datetime.datetime.now()


def compute_probability_click():
    # TODO: Implement Logic
    return 100


class RegisterProcedure(ApplicationSession):
    def onJoin(self, details):
        self.register(com_timeserver_now, 'com.timeserver.now')
        self.register(compute_probability_click, 'compute.probability.click')


runner = ApplicationRunner(url=CROSSBAR_URL, realm=CROSSBAR_REALM)
runner.run(RegisterProcedure)