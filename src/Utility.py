from datetime import datetime
import json
import math
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

__author__ = 'tusharmathur'


def flatten(_list):
    return sum(_list, [])


def join(_list, _str=' '):
    return _str.join(_list)


def convertToDataFrame(data, columns):
    return pd.DataFrame(data, columns=columns)


def convertJsonToDataFrame(jsonStr, columns):
    return convertToDataFrame(json.loads(jsonStr), columns=columns)


def convertIsoTimestampToDatetime(timestampRaw):
    return datetime.strptime(timestampRaw, '%Y-%m-%dT%H:%M:%S.%fZ')


def getSectionOfDay(timestamp: datetime):
    return math.floor(timestamp.hour / 6) + 1


def strCosineSimilarityScore(contextStrings, testStrings):
    wordList = [join(contextStrings), join(testStrings)]
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(wordList)
    result = cosine_similarity(matrix[0:1], matrix)[0][1]
    return result
