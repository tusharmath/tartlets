import json
import pickle

import src.Utility as u
from src.schemas.AdvertisementSchema import AdvertisementSchema


class SortAds:
    def __init__(self):
        self._adList = {}
        self._model = {}

    @property
    def model(self):
        return self._model

    @property
    def adList(self):
        return self._adList

    def warmUp(self, advertisementsRaw, modelRaw):
        self._adList = u.convertToDataFrame(json.loads(advertisementsRaw), columns=AdvertisementSchema)
        self._model = pickle.loads(modelRaw)


    def sortByCpm(self, searchContext, userTimestamp):
        searchContext = json.loads(searchContext)
        currentTime = u.convertIsoTimestampToDatetime(userTimestamp)


