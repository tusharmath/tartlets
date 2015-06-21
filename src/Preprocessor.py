from datetime import datetime
import functools
import json
import math

import pandas as pd
from sklearn import linear_model
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import src.schemas.AdImpressionSchema as impressionSchema


__author__ = 'tusharmathur'

DAY_SECTION_KEY = 'daySection'
CONTEXT_RELEVANCE = 'contextRelevance'
FEATURE_LIST = [
    impressionSchema.AD_ID,
    # impressionSchema.AD_KEYWORDS,
    # impressionSchema.SEARCH_CONTEXT,
    DAY_SECTION_KEY,
    CONTEXT_RELEVANCE
]


def flatten(_list):
    return sum(_list, [])


def join(_list, _str=' '):
    return _str.join(_list)


def groupByAdId(adImpressionsDF):
    return adImpressionsDF.groupby(impressionSchema.AD_ID)


def convertToDataFrame(_adImpressionsJSON):
    return pd.DataFrame(json.loads(_adImpressionsJSON), columns=impressionSchema.AdImpressionSchema)


def convertJavascriptTimestampToDatetime(timestampRaw):
    return datetime.strptime(timestampRaw, '%Y-%m-%dT%H:%M:%S.%fZ')


def getSectionOfDay(timestamp: datetime):
    return math.floor(timestamp.hour / 6) + 1


def computeDaySectionFeature(adImpressionsDF):
    return adImpressionsDF[impressionSchema.TIMESTAMP] \
        .map(convertJavascriptTimestampToDatetime) \
        .map(getSectionOfDay)


def strCosineSimilarityScore(contextStrings, testStrings):
    wordList = [join(contextStrings), join(testStrings)]
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(wordList)
    result = cosine_similarity(matrix[0:1], matrix)[0][1]
    return result


def computeContextRelevance(adImpressionsDF):
    context = impressionSchema.SEARCH_CONTEXT
    keywords = impressionSchema.AD_KEYWORDS
    score = strCosineSimilarityScore
    return adImpressionsDF.apply(lambda x: score(x[context], x[keywords]), axis=1)


def getCtrPredictionModel(_adImpressionsJSON):
    model = linear_model.LogisticRegression()

    adImpressionsDF = convertToDataFrame(_adImpressionsJSON)

    adImpressionsDF[CONTEXT_RELEVANCE] = computeContextRelevance(adImpressionsDF)
    adImpressionsDF[DAY_SECTION_KEY] = computeDaySectionFeature(adImpressionsDF)

    X = adImpressionsDF[FEATURE_LIST]
    Y = adImpressionsDF[impressionSchema.IS_CLICKED]

    X = X.join(pd.get_dummies(adImpressionsDF[impressionSchema.AD_ID], prefix='ad-id-'))
    X = X.join(pd.get_dummies(adImpressionsDF[DAY_SECTION_KEY], prefix='day-section-'))
    model.fit(X, Y)
    return model
