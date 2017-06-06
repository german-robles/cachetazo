import pytest
import sys
import datetime
from app.cachetazo import Cachetazo

@pytest.fixture
def cache():
    return Cachetazo()
@pytest.fixture
def big_cache():
    return Cachetazo(30)

def test_default_parameters(cache):
    assert cache.cache == {}
    assert cache.max_cache_size == 10

def test_max_cache_size(big_cache):
    assert big_cache.cache == {}
    assert big_cache.max_cache_size == 30

def test_cointains_magic_method(cache):
    assert cache.__contains__('myKey') == False
    cache.update('myNewKey', 'myNewValue')
    assert cache.__contains__('myNewKey') == True

def test_update(cache):
    cache.update('myNewKey', 'myNewValue')
    assert 'myNewKey' in cache.cache
    assert 'myNewValue' in cache.cache['myNewKey']['value']
    assert 'lad' in cache.cache['myNewKey']

def test_update_calls_lru(cache):
    dict = {
            'test': 'mykeyvalue',
            'red': 'apple',
            'grey': 'stone',
            'black': 'night',
            'sun': 'yellow',
            'six': 'sixtest',
            'seven': 'seventest',
            'eigth': 'eigthtest',
            'nine': 'ninetest',
            'ten': 'tentest'
           }
    for key in dict:
        cache.update(key, dict[key])
    cache.update('myNewKey', 'myNewValue')
    assert cache.size == 10
    assert 'test' not in cache.cache
    assert 'myNewKey' in cache.cache

def test_size(cache):
    dict ={ 'test': 'mykeyvalue', 'red': 'apple', 'grey': 'stone', 'black': 'night'}
    for key in dict:
        cache.update(key, dict[key])
    assert cache.size == 4
