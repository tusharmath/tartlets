import json

import pandas

from src.Preprocessor import groupByAdId
from src.schemas.AdImpressionSchema import AdImpressionSchema, IMPRESSION_ID
from mock.MockAdImpressions import MOCK_AD_IMPRESSION


__author__ = 'tusharmathur'


def TestGroupByAdId():
    df = pandas.DataFrame(json.loads(MOCK_AD_IMPRESSION), columns=AdImpressionSchema)
    fdByAdID = groupByAdId(df)
    print(groupByAdId(df)[IMPRESSION_ID].count())
    assert len(fdByAdID) == 2
    assert fdByAdID[IMPRESSION_ID].count()[0] == 2
    assert fdByAdID[IMPRESSION_ID].count()[1] == 1