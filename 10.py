from functools import wraps


def singleton(_class):
    constructor = _class.__new__
    initializer = _class.__init__

    @wraps(initializer)
    def no_init(self, *args, **kwargs):
        pass

    @wraps(constructor)
    def singleton_constructor(cls, *args, **kwargs):
        if _class.__instance__ is None:
            _class.__instance__ = constructor(cls)
            initializer(_class.__instance__)
        return _class.__instance__

    _class.__instance__ = None
    _class.__new__ = singleton_constructor
    _class.__init__ = no_init
    return _class


@singleton
class Counter():
    def __init__(self, value=3):
        self.value = value

    def inc(self):
        self.value += 1

    def get(self):
        return self.value


Counter(value=0).inc()
Counter(2).inc()
assert Counter().get() == 5
