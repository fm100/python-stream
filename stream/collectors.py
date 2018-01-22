def to_dict(key_func, value_func):
    """
    Returns a function which returns a dictionary by collecting the
    given iterable by key_func and value_func.  
    """
    def dict_collector(iterable):
        return {key_func(item): value_func(item) for item in iterable}
    return dict_collector


def groupby(key_func):
    """
    Returns a function which returns a dictionary by grouping the given
    iterable by key_func.
    """
    def grouper(iterable):
        result = {}
        for item in iterable:
            values = result.setdefault(key_func(item), [])
            values.append(item)
        return result
    return grouper
