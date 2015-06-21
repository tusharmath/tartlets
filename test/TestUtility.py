from datetime import datetime
import functools

import src.Utility as u


def TestConvertJavascriptTimestampToDatetime():
    a = u.convertJavascriptTimestampToDatetime('2015-06-20T19:25:47.487Z')
    b = datetime(2015, 6, 20, 19, 25, 47, 487000)
    assert a == b


def TestGetSectionOfDay():
    assert u.getSectionOfDay(datetime(2015, 6, 20, 19, 25, 47, 487000)) == 4
    assert u.getSectionOfDay(datetime(2015, 6, 20)) == 1
    assert u.getSectionOfDay(datetime(2015, 6, 20, 0, 30)) == 1
    assert u.getSectionOfDay(datetime(2015, 6, 20, 23, 30)) == 4


def TestStringRelevance():
    context = ['pretty', 'shoes']
    keywordList1 = ['shoes', 'shoes', 'shoes']
    keywordList2 = ['shoes', 'pretty', 'red']
    keywordList3 = ['apples', 'poop', 'shoes']
    keywordList4 = ['shoes', 'poop', 'preity']

    n = functools.partial(u.strCosineSimilarityScore, context)
    assert n(keywordList1) < n(keywordList2)
    assert n(keywordList1) > n(keywordList3)
    assert n(keywordList3) == n(keywordList4)

