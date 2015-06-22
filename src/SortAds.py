import json
import pickle

import src.Utility as u
from src.schemas.AdvertisementSchema import AdvertisementSchema


class SortAds:
    def __init__(self):
        self._adList = {}
        self._model = {}


    def warmUp(self, rawData):
        data = json.loads(rawData)
        self._adList = u.convertJsonToDataFrame(data['advertisements'], columns=AdvertisementSchema)
        self._model = pickle.loads(data['model'])


    def sortByCpm(self, searchContext, userTimestamp):
        searchContext = json.loads(searchContext)
        currentTime = u.convertIsoTimestampToDatetime(userTimestamp)



