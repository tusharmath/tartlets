import json
import jsonpickle
from mock.SerializedModel import SERIALIZED_MODEL
import src.schemas.AdvertisementSchema as x


def rawWarmUpParams():
    return {
        'model': SERIALIZED_MODEL,
        'advertisements': jsonpickle.encode([
            {x.ID: 1000, x.KEYWORDS: ['dog food', 'equator', 'fantastic'], x.BID: 50},
            {x.ID: 1001, x.KEYWORDS: ['dog food', 'equator', 'derpina'], x.BID: 150},
            {x.ID: 1001, x.KEYWORDS: ['dog food', 'cancer', 'fantastic'], x.BID: 10},
            {x.ID: 1000, x.KEYWORDS: ['dog food', 'generator', 'fantastic'], x.BID: 20}
        ])
    }