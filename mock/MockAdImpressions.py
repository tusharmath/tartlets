import json
import datetime
from src.schemas.AdImpressionSchema import IMPRESSION_ID

__author__ = 'tusharmathur'
currentTime = '2015-06-20T19:25:47.487Z'
MOCK_AD_IMPRESSION = json.dumps([
    {
        IMPRESSION_ID: '100',
        'advertisement': '1000',
        'timestamp': currentTime,
        'searchContext': ['a', 'b', 'c'],
        'adKeywords': ['a', 'b', 'c'],
        'adTitle': 'qwerty',
        'adSubtitle': 'opps',
        'adText': 'wendy had a little lamb',
        'adUrl': 'http://www.practo.com/bangalore/idiots',
        'isClicked': False
    },
    {
        IMPRESSION_ID: '101',
        'advertisement': '1000',
        'timestamp': currentTime,
        'searchContext': ['a', 'b', 'c'],
        'adKeywords': ['a', 'b', 'c'],
        'adTitle': 'qwerty',
        'adSubtitle': 'opps',
        'adText': 'wendy had a little lamb',
        'adUrl': 'http://www.practo.com/bangalore/idiots',
        'isClicked': False
    },
    {
        IMPRESSION_ID: '102',
        'advertisement': '1001',
        'timestamp': currentTime,
        'searchContext': ['a', 'b', 'c'],
        'adKeywords': ['a', 'b', 'c'],
        'adTitle': 'qwerty',
        'adSubtitle': 'opps',
        'adText': 'wendy had a little lamb',
        'adUrl': 'http://www.practo.com/bangalore/idiots',
        'isClicked': False
    }
])
