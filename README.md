[![Build Status](https://travis-ci.org/fm100/python-stream.svg?branch=master)](https://travis-ci.org/fm100/python-stream)
[![codecov](https://codecov.io/gh/fm100/python-stream/branch/master/graph/badge.svg)](https://codecov.io/gh/fm100/python-stream)

# python-stream (simplestream)
Stream pipeline API with lazy evaluation inspired by Java 8

## Install
```
pip install simplestream
```

## Example 1
```
>>> from stream import Stream
>>>
>>> l = Stream(range(10))\
...     .filter(lambda x: x % 2 == 0)\
...     .map(lambda x: x ** 2)\
...     .collect(list)
>>> print(l)
[0, 4, 16, 36, 64]
>>>
```

## Example 2
```
>>> from stream import Stream
>>>
>>> s = Stream('Hello').collect(','.join)
>>> print(s)
H,e,l,l,o
>>>
```

## Example 3
```
>>> from stream import Stream
>>>
>>> s1 = Stream(range(5))\
...     .map(lambda x: x * 2)
>>> s2 = Stream(range(3))\
...     .flatmap(range)
>>> Stream.chain(s1, s2).collect(list)
[0, 2, 4, 6, 8, 0, 0, 1]
>>>
```

## APIs
### Transformations
* map
* filter
* flatten
* flatmap
* distinct
* limit
* skip
* chain

### Actions
* all
* any
* none
* min
* max
* count
* reduce
* foreach
* collect

## Note
* Every stream API is lazily evaluated, so until you call action API, functions you passed to transformations will not be called.
* Unlike Java 8 Stream API, min and max get key function instead of comparator.
* Instead of concat, simplestream provides chain method which gets arbitrary number of streams.
