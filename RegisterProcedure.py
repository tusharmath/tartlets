from autobahn.asyncio.wamp import ApplicationSession
from autobahn.asyncio.wamp import ApplicationRunner
import datetime

# CONSTANTS
CROSSBAR_REALM = u"async-worker"
CROSSBAR_URL = u"ws://localhost:8080/ws"


# RPC
def timeserverNow():
    return datetime.datetime.now()


def computeCtrPredictionModel(adImpressions):
    # TODO: Implement Logic
    return 100


def computeCpm(searchPhrases, qualifyingAds, currentTime):
    # TODO: Implement Logic
    return 100


class RegisterProcedure(ApplicationSession):
    def onJoin(self, details):
        self.register(timeserverNow, 'com.timeserver.now')
        self.register(computeCtrPredictionModel, 'compute.ctr')
        self.register(computeCpm, 'compute.cpm')


runner = ApplicationRunner(url=CROSSBAR_URL, realm=CROSSBAR_REALM)
runner.run(RegisterProcedure)