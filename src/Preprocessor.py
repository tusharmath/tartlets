from datetime import datetime
import json
import pandas as pd

from src.schemas.AdImpressionSchema import AdImpressionSchema, AD_ID, IMPRESSION_ID, IS_CLICKED, TIMESTAMP


__author__ = 'tusharmathur'


def groupByAdId(adImpressionsDF):
    return adImpressionsDF.groupby(AD_ID)


def convertToDataFrame(_adImpressionsJSON):
    return pd.DataFrame(json.loads(_adImpressionsJSON), columns=AdImpressionSchema)


def convertJavascriptTimestampToDatetime(timestampJS):
    return datetime.strptime(timestampJS, '%Y-%m-%dT%H:%M:%S.%fZ')


    return 10