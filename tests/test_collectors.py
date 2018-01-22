from stream import Stream
from stream import collectors


class TestCollectors:
    def test_to_dict(self):
        expected = {'a': 1, 'bb': 2, 'ccc': 3}
        actual = Stream(['a', 'bb', 'ccc']) \
            .collect(collectors.to_dict(lambda _: _, len))
        assert expected == actual

    def test_groupby(self):
        expected = {1: ['a', 'A'], 2: ['bb', 'BB'], 3: ['ccc', 'CCC']}
        actual = Stream(['a', 'bb', 'ccc', 'A', 'BB', 'CCC']) \
            .collect(collectors.groupby(len))
        assert expected == actual
