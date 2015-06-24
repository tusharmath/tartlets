import json
import datetime
import src.schemas.AdImpressionSchema as impr

__author__ = 'tusharmathur'
MOCK_CLICK_THROUGH_RATE = [
    [0.7514943912329435, 0.24850560876705657],
    [0.7369502408155573, 0.2630497591844427],
    [0.3609419142315772, 0.6390580857684228]
]

MOCK_AD_IMPRESSION = json.dumps([
    {
        impr.IMPRESSION_ID: '100',
        impr.AD_ID: '1000',
        impr.TIMESTAMP: '2015-06-20T19:25:47.487Z',
        impr.SEARCH_CONTEXT: ['a', 'banana', 'cherry'],
        impr.AD_KEYWORDS: ['apple', 'banana', 'cherry'],
        impr.AD_TITLE: 'qwerty',
        impr.AD_SUBTITLE: 'opps',
        impr.AD_TEXT: 'wendy had a little lamb',
        impr.AD_URL: 'http://www.practo.com/bangalore/idiots',
        impr.IS_CLICKED: False
    },
    {
        impr.IMPRESSION_ID: '101',
        impr.AD_ID: '1000',
        impr.TIMESTAMP: '2015-06-20T10:25:47.487Z',
        impr.SEARCH_CONTEXT: ['d', 'equator', 'f'],
        impr.AD_KEYWORDS: ['dog food', 'equator', 'fantastic'],
        impr.AD_TITLE: 'qwerty',
        impr.AD_SUBTITLE: 'opps',
        impr.AD_TEXT: 'wendy had a little lamb',
        impr.AD_URL: 'http://www.practo.com/bangalore/idiots',
        impr.IS_CLICKED: False
    },
    {
        impr.IMPRESSION_ID: '102',
        impr.AD_ID: '1001',
        impr.TIMESTAMP: '2015-06-20T01:25:47.487Z',
        impr.SEARCH_CONTEXT: ['a', 'b', 'c'],
        impr.AD_KEYWORDS: ['goat meat', 'horse shit', 'idiots'],
        impr.AD_TITLE: 'qwerty',
        impr.AD_SUBTITLE: 'opps',
        impr.AD_TEXT: 'wendy had a little lamb',
        impr.AD_URL: 'http://www.practo.com/bangalore/idiots',
        impr.IS_CLICKED: True
    }
])
