# Cachetazo
This is a very simple cache key, value for Python with LRU by Datetime

### Version
0.0.1

### Tech

Cachetazo use:

* [Python]


### Installation

Clone the repo

```sh
git clone https://github.com/german-robles/cachetazo.git
```

### Creating an example code:
```python
from app.cachetazo import Cachetazo
 #creating an instance:
 cache = Cachetazo() # By default the instance will create a cache with max_cache_size = 10.
                     # You can change this on intance time = Cachetazo(30) , now will be max_cache_size = 30

 # Adding a new key value:
 cache.update('myKey', 'myvalue')

 # Getting all cache size:
 print cache.size

 # Printing all cache objects:
 print cache.cache

 # Getting max_cache_size
 print cache.max_cache_size
```
### Contributing adding new features:

#### Using [Make] and  [Docker] to test our application

##### First you must build the container

```sh
  make build #run this on root dir of this repo
```
##### Then test your added tests and check the report_html to get coverage metrics:

```sh
  make testing #run this on root dir of this repo
```
   [Python]: <https://www.python.org/>
   [Docker]: <https://www.docker.com/>
   [Make]: <https://www.gnu.org/software/make/manual/make.html>
