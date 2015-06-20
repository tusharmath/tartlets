import json
import datetime
import src.schemas.AdImpressionSchema as impressionSchema

__author__ = 'tusharmathur'
MOCK_AD_IMPRESSION = json.dumps([
    {
        (impressionSchema.IMPRESSION_ID): '100',
        'advertisement': '1000',
        'timestamp': '2015-06-20T19:25:47.487Z',
        'searchContext': ['a', 'b', 'c'],
        'adKeywords': ['a', 'b', 'c'],
        'adTitle': 'qwerty',
        'adSubtitle': 'opps',
        'adText': 'wendy had a little lamb',
        'adUrl': 'http://www.practo.com/bangalore/idiots',
        'isClicked': False
    },
    {
        (impressionSchema.IMPRESSION_ID): '101',
        'advertisement': '1000',
        'timestamp': '2015-06-20T10:25:47.487Z',
        'searchContext': ['a', 'b', 'c'],
        'adKeywords': ['a', 'b', 'c'],
        'adTitle': 'qwerty',
        'adSubtitle': 'opps',
        'adText': 'wendy had a little lamb',
        'adUrl': 'http://www.practo.com/bangalore/idiots',
        'isClicked': False
    },
    {
        (impressionSchema.IMPRESSION_ID): '102',
        'advertisement': '1001',
        'timestamp': '2015-06-20T01:25:47.487Z',
        'searchContext': ['a', 'b', 'c'],
        'adKeywords': ['a', 'b', 'c'],
        'adTitle': 'qwerty',
        'adSubtitle': 'opps',
        'adText': 'wendy had a little lamb',
        'adUrl': 'http://www.practo.com/bangalore/idiots',
        'isClicked': False
    }
])
