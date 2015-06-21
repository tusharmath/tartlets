import pandas as pd
from sklearn import linear_model
import src.Utility as u
import src.schemas.AdImpressionSchema as impressionSchema

__author__ = 'tusharmathur'

DAY_SECTION_KEY = 'daySection'
CONTEXT_RELEVANCE = 'contextRelevance'
FEATURE_LIST = [
    CONTEXT_RELEVANCE
]


def groupByAdId(adImpressionsDF):  # TODO: Make it more generic
    return adImpressionsDF.groupby(impressionSchema.AD_ID)


def computeDaySectionFeature(adImpressionsDF):
    return adImpressionsDF[impressionSchema.TIMESTAMP] \
        .map(u.convertJavascriptTimestampToDatetime) \
        .map(u.getSectionOfDay)


def computeContextRelevanceFeature(adImpressionsDF):
    context = impressionSchema.SEARCH_CONTEXT
    keywords = impressionSchema.AD_KEYWORDS
    score = u.strCosineSimilarityScore
    return adImpressionsDF.apply(lambda x: score(x[context], x[keywords]), axis=1)


def getCtrPredictionModel(_adImpressionsJSON):
    model = linear_model.LogisticRegression()
    adImpressionsDF = u.convertJsonToDataFrame(_adImpressionsJSON, impressionSchema.AdImpressionSchema)

    adImpressionsDF[CONTEXT_RELEVANCE] = computeContextRelevanceFeature(adImpressionsDF)
    adImpressionsDF[DAY_SECTION_KEY] = computeDaySectionFeature(adImpressionsDF)

    Y = adImpressionsDF[impressionSchema.IS_CLICKED]
    X = adImpressionsDF[FEATURE_LIST] \
        .join(pd.get_dummies(adImpressionsDF[impressionSchema.AD_ID], prefix=impressionSchema.AD_ID)) \
        .join(pd.get_dummies(adImpressionsDF[DAY_SECTION_KEY], prefix=DAY_SECTION_KEY))
    model.fit(X, Y)
    return model
