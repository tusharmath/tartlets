from datetime import datetime
import json

import pandas
import src.Preprocessor as base
import src.schemas.AdImpressionSchema as impressionSchema
from mock.MockAdImpressions import MOCK_AD_IMPRESSION


__author__ = 'tusharmathur'


def TestGroupByAdId():
    df = pandas.DataFrame(json.loads(MOCK_AD_IMPRESSION), columns=impressionSchema.AdImpressionSchema)
    fdByAdID = base.groupByAdId(df)
    assert len(fdByAdID) == 2
    assert fdByAdID[impressionSchema.IMPRESSION_ID].count()[0] == 2
    assert fdByAdID[impressionSchema.IMPRESSION_ID].count()[1] == 1


def TestConvertJavascriptTimestampToDatetime():
    a = base.convertJavascriptTimestampToDatetime('2015-06-20T19:25:47.487Z')
    b = datetime(2015, 6, 20, 19, 25, 47, 487000)
    assert a == b


def TestGetSectionOfDay():
    assert base.getSectionOfDay(datetime(2015, 6, 20, 19, 25, 47, 487000)) == 4
    assert base.getSectionOfDay(datetime(2015, 6, 20)) == 1
    assert base.getSectionOfDay(datetime(2015, 6, 20, 0, 30)) == 1
    assert base.getSectionOfDay(datetime(2015, 6, 20, 23, 30)) == 4


def TestTemp():
    assert base.computeDaySection()