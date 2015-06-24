from mock.SerializedModel import SERIALIZED_MODEL_COEF
from src.CtrPredictionModel import CtrPredictionModel
import src.Utility as u
import src.schemas.AdImpressionSchema as impressionSchema
from mock.MockAdImpressions import MOCK_AD_IMPRESSION


__author__ = 'tusharmathur'


def TestGroupByAdId():
    df = u.convertJsonToDataFrame(MOCK_AD_IMPRESSION, impressionSchema.AdImpressionSchema)
    fdByAdID = CtrPredictionModel.groupByAdId(df)
    assert len(fdByAdID) == 2
    assert fdByAdID[impressionSchema.IMPRESSION_ID].count()[0] == 2
    assert fdByAdID[impressionSchema.IMPRESSION_ID].count()[1] == 1


def TestTrain():
    item = CtrPredictionModel()
    model = item.train(MOCK_AD_IMPRESSION)
    assert SERIALIZED_MODEL_COEF == model.coef_[0].tolist()
    assert item.model == model