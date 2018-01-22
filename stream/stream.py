import functools
import itertools


class Stream:
    """Stream pipeline API inspired by Java 8 stream"""

    def __init__(self, iterable, generator=next):
        self.iterator = iter(iterable)
        self.generator = generator

    def __iter__(self):
        return self

    def __next__(self):
        """To support python 3"""
        return self.next()

    def next(self):
        return self.generator(self.iterator)

    def map(self, mapper):
        """
        Returns a stream consisting of the results of applying the
        given function to the items of this stream.
        """
        def _map(iterator):
            return mapper(next(iterator))
        return self.__class__(self, _map)

    def filter(self, predicate):
        """
        Returns a stream consisting of the items of this stream that
        match the given predicate.
        """
        def _filter(iterator):
            while True:
                item = next(iterator)
                if predicate(item):
                    return item
        return self.__class__(self, _filter)

    def flatten(self):
        """
        Returns a stream consisting of the flattened items of this
        stream.
        """
        return self.__class__(itertools.chain.from_iterable(self))

    def flatmap(self, mapper):
        """
        Returns a stream consisting of the flattened items of the
        results of applying the given function to the items of this
        stream.
        """
        return self.map(mapper).flatten()

    def distinct(self):
        """
        Returns a stream consisting of the distinct items of this
        stream.
        """
        memory = set()

        def _distinct(iterator):
            while True:
                item = next(iterator)
                if item in memory:
                    continue
                memory.add(item)
                return item
        return self.__class__(self, _distinct)

    def limit(self, max_size):
        """
        Returns a stream consisting of items of this stream, truncated
        to be no longer than max_size in length.
        """
        return self.__class__(itertools.islice(self, max_size))

    def skip(self, n):
        """
        Returns a stream consisting of remaining items of this stream
        after discarding first n items.
        """
        return self.__class__(itertools.islice(self, n, None))

    def all(self, predicate):
        """
        Returns True if all items of this stream match the given
        predicate, otherwise False.
        """
        return all(predicate(item) for item in self)

    def any(self, predicate):
        """
        Returns True if any items of this stream match the given
        predicate, otherwise False.
        """
        return any(predicate(item) for item in self)

    def none(self, predicate):
        """
        Returns True if no items of this stream match the given
        predicate, otherwise False.
        """
        return not self.any(predicate)

    def min(self, key=lambda _: _):
        """
        Returns the smallest item of this stream.
         
        :param key: function of one argument that is used to extract
        comparison key from each item of this stream 
        """
        return min(self, key=key)

    def max(self, key=lambda _: _):
        """
        Returns the largest item of this stream.
        
        :param key: function of one argument that is used to extract
        comparison key from each item of this stream
        """
        return max(self, key=key)

    def count(self):
        """Returns the number of items of this stream."""
        return sum(1 for _ in self)

    def reduce(self, binary_operator):
        """
        Apply a function of two arguments cumulatively to the items of
        this stream from left to right, so as to reduce this stream to
        a single value.
        """
        return functools.reduce(binary_operator, self)

    def foreach(self, action):
        """Performs an action for each items of this stream."""
        for item in self:
            action(item)

    def collect(self, collector):
        """
        Returns a collection of items collected by given collector.
        """
        return collector(self)

    @staticmethod
    def chain(*streams):
        """Returns concatenated stream of given streams."""
        return Stream(itertools.chain(*streams))
