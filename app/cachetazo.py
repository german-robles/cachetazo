#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

class Cachetazo(object):
    """
	CACHETAZO cache for python
    """
    __author__ = "Germán Robles"
    __license__ = "GNU"
    __version__ = "0.0.1"
    __email__ = "ger.robles89@gmail.com"
    __status__ = "beta"

    def __init__(self, max_cache_size=10):
        self.cache = {}
        self.max_cache_size = max_cache_size

    def __contains__(self, k):
        return k in self.cache

    def lru(self):
        lru = None
        for k in self.cache:
            if lru is None:
                lru = k
            elif self.cache[k]['lad'] < self.cache[lru][
                'lad']:
                lru = k
        self.cache.pop(lru)

    def update(self, k, v):
        if k not in self.cache and len(self.cache) >= self.max_cache_size:
            self.lru()
            #lad == Last Accessed Date
        self.cache[k] = {'lad': datetime.datetime.now(),
                           'value': v}
    @property
    def size(self):
        return len(self.cache)
