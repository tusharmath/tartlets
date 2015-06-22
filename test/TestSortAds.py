from mock.RawWarmupData import rawWarmUpParams
from mock.SerializedModel import SERIALIZED_MODEL_COEF
from src.SortAds import SortAds


def TestWarmUp():
    params = rawWarmUpParams()
    adSorter = SortAds()
    adSorter.adList = params['advertisements']
    adSorter.model = params['model']
    adSorter._adList
    assert SERIALIZED_MODEL_COEF == adSorter.model.coef_[0].tolist()
    assert len(adSorter.adList) == 4