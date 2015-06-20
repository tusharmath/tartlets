from datetime import datetime
import json
import math
import pandas as pd
import pickle
import sklearn
import src.schemas.AdImpressionSchema as impressionSchema

__author__ = 'tusharmathur'

DAY_SECTION_KEY = 'daySection'
FEATURE_LIST = (impressionSchema.AD_KEYWORDS,
                impressionSchema.SEARCH_CONTEXT,
                impressionSchema.AD_SUBTITLE,
                impressionSchema.AD_TEXT,
                DAY_SECTION_KEY)


def groupByAdId(adImpressionsDF):
    return adImpressionsDF.groupby(impressionSchema.AD_ID)


def convertToDataFrame(_adImpressionsJSON):
    return pd.DataFrame(json.loads(_adImpressionsJSON), columns=impressionSchema.AdImpressionSchema)


def convertJavascriptTimestampToDatetime(timestampRaw):
    return datetime.strptime(timestampRaw, '%Y-%m-%dT%H:%M:%S.%fZ')


def getSectionOfDay(timestamp: datetime):
    return math.floor(timestamp.hour / 6) + 1


def computeDaySection(adImpressionsDF):
    return adImpressionsDF[impressionSchema.TIMESTAMP] \
        .map(convertJavascriptTimestampToDatetime) \
        .map(getSectionOfDay)


def getCtrPredictionModel(_adImpressionsJSON):
    model = sklearn.linear_model.LogisticRegression()

    adImpressionsDF = convertToDataFrame(_adImpressionsJSON)
    adImpressionsDF[DAY_SECTION_KEY] = computeDaySection(adImpressionsDF)

    X = adImpressionsDF[FEATURE_LIST]
    Y = adImpressionsDF[impressionSchema.IS_CLICKED]

    dummyCodedAdID = pd.get_dummies(impressionSchema.AD_ID, prefix='ad-id-')
    dummyCodedDaySection = pd.get_dummies(DAY_SECTION_KEY, prefix='day-section-')
    X =X.join(dummyCodedAdID)
    X= X.join(dummyCodedDaySection)
    model.fit(X, Y)
    return pickle.dumps(model)