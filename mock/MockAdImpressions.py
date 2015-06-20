import json
from xmlrpc.client import DateTime

__author__ = 'tusharmathur'
MOCK_AD_IMPRESSION = json.dumps([
    {
        '_id': '100',
        'timestamp': DateTime('01-01-01'),
        'searchContext': ['a', 'b', 'c'],
        'adKeywords': ['a', 'b', 'c'],
        'adTitle': 'qwerty',
        'adSubtitle': 'opps',
        'adText': 'wendy had a little lamb',
        'adUrl': 'http://www.practo.com/bangalore/idiots',
        'isClicked': False
    },
    {
        '_id': '100',
        'timestamp': DateTime('01-01-01'),
        'searchContext': ['a', 'b', 'c'],
        'adKeywords': ['a', 'b', 'c'],
        'adTitle': 'qwerty',
        'adSubtitle': 'opps',
        'adText': 'wendy had a little lamb',
        'adUrl': 'http://www.practo.com/bangalore/idiots',
        'isClicked': False
    },
    {
        '_id': '101',
        'timestamp': DateTime('01-01-01'),
        'searchContext': ['a', 'b', 'c'],
        'adKeywords': ['a', 'b', 'c'],
        'adTitle': 'qwerty',
        'adSubtitle': 'opps',
        'adText': 'wendy had a little lamb',
        'adUrl': 'http://www.practo.com/bangalore/idiots',
        'isClicked': False
    }
])
