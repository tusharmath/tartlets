from datetime import datetime
import functools
import json

import pandas
import src.Preprocessor as base
import src.schemas.AdImpressionSchema as impressionSchema
from mock.MockAdImpressions import MOCK_AD_IMPRESSION


__author__ = 'tusharmathur'


def getMockImpressionsAsDF():
    return pandas.DataFrame(json.loads(MOCK_AD_IMPRESSION), columns=impressionSchema.AdImpressionSchema)


def TestGroupByAdId():
    df = getMockImpressionsAsDF()
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


def TestStringRelevance():
    context = ['pretty', 'shoes']
    keywordList1 = ['shoes', 'shoes', 'shoes']
    keywordList2 = ['shoes', 'pretty', 'red']
    keywordList3 = ['apples', 'poop', 'shoes']
    keywordList4 = ['shoes', 'poop', 'preity']

    n = functools.partial(base.strCosineSimilarityScore, context)
    assert n(keywordList1) < n(keywordList2)
    assert n(keywordList1) > n(keywordList3)
    assert n(keywordList3) == n(keywordList4)


