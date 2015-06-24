import pandas as pd
from sklearn import linear_model

import src.Utility as u

import src.schemas.AdImpressionSchema as impressionSchema


__author__ = 'tusharmathur'


class CtrPredictionModel(object):
    def __init__(self):
        self.model = None
        self.DAY_SECTION_KEY = 'daySection'
        self.CONTEXT_RELEVANCE = 'contextRelevance'
        self.FEATURE_LIST = [
            self.CONTEXT_RELEVANCE
        ]

    @staticmethod
    def groupByAdId(adImpressionsDF):  # TODO: Make it more generic
        return adImpressionsDF.groupby(impressionSchema.AD_ID)

    @staticmethod
    def computeDaySectionFeature(adImpressionsDF):
        return adImpressionsDF[impressionSchema.TIMESTAMP] \
            .map(u.convertIsoTimestampToDatetime) \
            .map(u.getSectionOfDay)

    @staticmethod
    def computeContextRelevanceFeature(adImpressionsDF):
        context = impressionSchema.SEARCH_CONTEXT
        keywords = impressionSchema.AD_KEYWORDS
        score = u.strCosineSimilarityScore
        return adImpressionsDF.apply(lambda x: score(x[context], x[keywords]), axis=1)

    def train(self, _adImpressionsJSON):
        model = linear_model.LogisticRegression()
        impressionsDF = u.convertJsonToDataFrame(_adImpressionsJSON, impressionSchema.AdImpressionSchema)

        features = self.createAdImpressionFeatures(_adImpressionsJSON)
        target = impressionsDF[impressionSchema.IS_CLICKED]
        model.fit(features, target)
        self.model = model
        return model

    def createAdImpressionFeatures(self, _adImpressionsJSON):
        impressionsDF = u.convertJsonToDataFrame(_adImpressionsJSON, impressionSchema.AdImpressionSchema)

        impressionsDF[self.CONTEXT_RELEVANCE] = self.computeContextRelevanceFeature(impressionsDF)
        impressionsDF[self.DAY_SECTION_KEY] = self.computeDaySectionFeature(impressionsDF)

        return impressionsDF[self.FEATURE_LIST] \
            .join(pd.get_dummies(impressionsDF[impressionSchema.AD_ID], prefix=impressionSchema.AD_ID)) \
            .join(pd.get_dummies(impressionsDF[self.DAY_SECTION_KEY], prefix=self.DAY_SECTION_KEY))

    def predict(self, _adImpressionsJSON):
        features = self.createAdImpressionFeatures(_adImpressionsJSON)
        return self.model.predict_proba(features).tolist()