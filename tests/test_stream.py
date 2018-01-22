import sys
from unittest.mock import call
from unittest.mock import patch

from stream import Stream


class TestStream:
    def test_map(self):
        expected = [1, 4, 9]
        actual = Stream([1, 2, 3]) \
            .map(lambda x: x ** 2) \
            .collect(list)
        assert expected == actual

    def test_filter(self):
        expected = [1, 3, 5]
        actual = Stream([1, 2, 3, 4, 5]) \
            .filter(lambda x: x % 2 != 0) \
            .collect(list)
        assert expected == actual

    def test_flatten(self):
        expected = [1, 2, 3, 4, 5]
        actual = Stream([[1, 2], [3, 4, 5]]) \
            .flatten() \
            .collect(list)
        assert expected == actual

    def test_flatmap(self):
        expected = [0, 0, 1, 0, 1, 2]
        actual = Stream([1, 2, 3]) \
            .flatmap(range) \
            .collect(list)
        assert expected == actual

    def test_distinct(self):
        expected = [1, 2, 3, 4]
        actual = Stream([1, 2, 3, 3, 4, 4]) \
            .distinct() \
            .collect(list)
        assert expected == actual

    def test_limit(self):
        expected = [1, 2, 3]
        actual = Stream([1, 2, 3, 4, 5]) \
            .limit(3) \
            .collect(list)
        assert expected == actual

    def test_skip(self):
        expected = [3, 4, 5]
        actual = Stream([1, 2, 3, 4, 5]) \
            .skip(2) \
            .collect(list)
        assert expected == actual

    def test_all(self):
        assert Stream([1, 2, 3, 4, 5]).all(lambda x: x > 0)
        assert not Stream([1, 2, 3, 4, 5]).all(lambda x: x % 2 == 0)

    def test_any(self):
        assert Stream([1, 2, 3, 4, 5]).any(lambda x: x > 0)
        assert Stream([1, 2, 3, 4, 5]).any(lambda x: x % 2 == 0)
        assert not Stream([1, 2, 3, 4, 5]).any(lambda x: x < 0)

    def test_none(self):
        assert not Stream([1, 2, 3, 4, 5]).none(lambda x: x > 0)
        assert not Stream([1, 2, 3, 4, 5]).none(lambda x: x % 2 == 0)
        assert Stream([1, 2, 3, 4, 5]).none(lambda x: x < 0)

    def test_min(self):
        assert Stream([3, 1, 2, 5, 4]).min() == 1
        assert Stream(['aaa', 'bb', 'c']).min() == 'aaa'
        assert Stream(['aaa', 'bb', 'c']).min(key=len) == 'c'

    def test_max(self):
        assert Stream([3, 1, 2, 5, 4]).max() == 5
        assert Stream(['aaa', 'bb', 'c']).max() == 'c'
        assert Stream(['aaa', 'bb', 'c']).max(key=len) == 'aaa'

    def test_count(self):
        assert Stream([2, 3, 4, 5]).count() == 4
        assert Stream([1, 2, 3, 4, 5]).count() == 5

    def test_reduce(self):
        expected = 120
        actual = Stream([1, 2, 3, 4, 5]).reduce(lambda x, y: x * y)
        assert expected == actual

    def test_foreach(self):
        with patch('sys.stdout.write') as mock_print:
            Stream(['a', 'b', 'c']).foreach(sys.stdout.write)
            mock_print.assert_has_calls([call('a'), call('b'), call('c')])
