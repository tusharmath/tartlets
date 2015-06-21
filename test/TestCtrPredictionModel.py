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


def TestGetCtrPredictionModel():
    item = CtrPredictionModel()
    x = [
        -0.27621892378767104,
        -0.5115574973374354,
        0.3609452685495564,
        0.3609452685495564,
        -0.2630502211274582,
        -0.2485072762099772
    ]

    y = item.getModel(MOCK_AD_IMPRESSION).coef_[0].tolist()
    assert x == y