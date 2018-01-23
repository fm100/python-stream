[![Build Status](https://travis-ci.org/fm100/python-stream.svg?branch=master)](https://travis-ci.org/fm100/python-stream)

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

## APIs
### Transformations
* map
* filter
* flatten
* flatmap
* distinct
* limit
* skip

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
