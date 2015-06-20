import json
import pandas as pd

from src.schemas.AdImpressionSchema import AdImpressionSchema, AD_ID


__author__ = 'tusharmathur'


def groupByAdId(adImpressionsDF):
    return adImpressionsDF.groupby(AD_ID)

def mapAdIdToCategoricalValue(_adImpressionsJSON):
    adImpressionsDF = pd.DataFrame(json.loads(_adImpressionsJSON), columns=AdImpressionSchema)
    adImpressionsDF.groupby(AD_ID)
    return 10