## 0x01-caching
### Learning Objectives
#### General
* What a caching system is
* What FIFO means
* What LIFO means
* What LRU means
* What MRU means
* What LFU means

### caching systems
* A caching system is a temporary storage area for frequently accessed data that is used to speed up the process of retrieving data.
* Caching systems store a copy of the data that is stored elsewhere, such as in a database, so that when the data is needed, it can be quickly retrieved from the cache rather than the slower and more time-consuming process of accessing the original storage location.

### FIFO
* FIFO stands for First In, First Out, and is a method for managing data in a cache.
* In a FIFO cache, the first item that is added to the cache is the first item that is removed when the cache is full and a new item needs to be added.

### LIFO
* LIFO stands for Last In, First Out, and is another method for managing data in a cache.
* In a LIFO cache, the last item that is added to the cache is the first item that is removed when the cache is full and a new item needs to be added.

### LRU
* LRU stands for Least Recently Used, and is a method for managing data in a cache.
* In an LRU cache, the item that has not been accessed for the longest period of time is the item that is removed when the cache is full and a new item needs to be added.

### MRU
* MRU stands for Most Recently Used, and is another method for managing data in a cache.
* In an MRU cache, the item that has been accessed most recently is the item that is removed when the cache is full and a new item needs to be added.

### LFU
* LFU stands for Least Frequently Used, and is a method for managing data in a cache.
* In an LFU cache, the item that has been accessed the least number of times is the item that is removed when the cache is full and a new item needs to be added.

### Resources
* [Caching system](https://en.wikipedia.org/wiki/Cache_(computing))
* [FIFO](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics))
* [LIFO](https://en.wikipedia.org/wiki/LIFO_(computing))
* [LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU))
* [MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_recently_used_(MRU))
* [LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-frequently_used_(LFU))
* [Redis](https://redis.io/)