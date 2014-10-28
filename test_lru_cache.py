import pytest
import sys
from lru_cache import LRUNode, LRUCache

@pytest.fixture(scope="function")
def create_full_cache():
    my_cache = LRUCache()
    test_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for num in test_list:
        my_cache.set(num)
    return my_cache

def test_get_data():
    empty_cache = LRUCache()
    assert empty_cache.get("BUM") == "BUM_MY_TEST_DATA"
    assert empty_cache._size == 1
    assert empty_cache._head == empty_cache._dict["BUM"]

    assert empty_cache.get("BUM2") == "BUM2_MY_TEST_DATA"
    assert empty_cache._size == 2
    assert empty_cache._head == empty_cache._dict["BUM2"]
    assert empty_cache._tail == empty_cache._dict["BUM"]


def test_change_prio(create_full_cache):
    tmp_cache = create_full_cache
    assert tmp_cache.get(4) == "4_MY_TEST_DATA"
    assert tmp_cache.get(15) == "15_MY_TEST_DATA"
    assert tmp_cache._head == tmp_cache._dict[15]
    assert tmp_cache._tail == tmp_cache._dict[1]

    assert tmp_cache.get(16) == "16_MY_TEST_DATA"
    assert tmp_cache._head == tmp_cache._dict[16]
    assert tmp_cache._dict.get(1, "NODATA") == "NODATA"

    tmp_cache.get(4)
    assert tmp_cache._head == tmp_cache._dict.get(4)


def test_remove_node(create_full_cache):
    tmp_cache = create_full_cache
    assert tmp_cache._tail == tmp_cache._dict[1]
    tmp_cache.remove_last_node()
    assert tmp_cache._dict[2] == tmp_cache._tail
    assert tmp_cache._dict.get(1, "NODATA") == "NODATA"

    tmp2_cache = LRUCache()
    tmp2_cache.set(20)
    tmp2_cache.set(21)
    tmp2_cache.remove_last_node()
    assert tmp2_cache._head == tmp2_cache._dict[21]
    assert tmp2_cache._tail == None
    tmp2_cache.remove_last_node()
    assert tmp2_cache._head == None
    assert tmp2_cache._tail == None










