import json
import datetime
import src.schemas.AdImpressionSchema as impr

__author__ = 'tusharmathur'

MOCK_AD_IMPRESSION = json.dumps([
    {
        impr.IMPRESSION_ID: '100',
        impr.AD_ID: '1000',
        impr.TIMESTAMP: '2015-06-20T19:25:47.487Z',
        impr.SEARCH_CONTEXT: ['a', 'b', 'c'],
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
        impr.SEARCH_CONTEXT: ['d', 'e', 'f'],
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
        impr.IS_CLICKED: False
    }
])
