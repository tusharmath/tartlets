import json
import pickle

import src.Utility as u
from src.schemas.AdvertisementSchema import AdvertisementSchema


class SortAds:
    _model = None
    _adList = None

    @property
    def model(self):
        return self._model

    @property
    def adList(self):
        return self._adList

    @adList.setter
    def adList(self, advertisementRaw):
        self._adList = u.convertToDataFrame(json.loads(advertisementRaw), columns=AdvertisementSchema)


    @model.setter
    def model(self, modelRaw):
        self._model = pickle.loads(modelRaw)


    def sortByCpm(self, searchContext, userTimestamp):
        searchContext = json.loads(searchContext)
        currentTime = u.convertIsoTimestampToDatetime(userTimestamp)


