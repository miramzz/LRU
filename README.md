LRU (Least Recently Used) Cache Implementation
***********************************************
This is a cache with fixed size in terms of the number of items it holds (supplied at instantiation).The cache must allow client code to get items from the cache and store
items to the cache. Once the cache is full, when the client wants to store a new item
in the cache, an old item must be overwritten or removed to make room. The item we will remove is the Least Recently Used (LRU) item.

How it works?
lru_cache stores every request as a node in a doubly link list.
Doubly link list head stores most recent requested data and tail
stores the least recent requested data.
When user sends a request, lru_cahe takes the request as key value
and creates the data. If this data has not already stored in the cache,
it adds the data to cache dictionary.
With every new request lru_cache updates priority of the datas stored in
cache. If cache is full, it removes the oldest data and add the new request

How Test file works?
To run test file simply put all files in one directory.
pip install pytest
run py.test
test_get_data, tests get and add functionality in the code
test_change_prio and test_remove_node simply test their own functions
