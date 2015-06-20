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
    """
    Features:
    1. Timestamp: Hashed with 8 categorical values
    2. Cosine Similarity: Search Phrases & Ad Target Phrases
    3. Search Phrase: Hashed with n categorical values
    4. Ad ID: Hashed with n categorical values, where n = count(ad) where ad.impressions > threshold
    """

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