def singleton(cls, *args, **kw):
    instance = {}

    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]

    return _singleton


@singleton
class test_singleton(object):
    def __init__(self):
        self.num_sum = 0

    def show(self):
        return self.num_sum

    def add(self):
        self.num_sum = 100


if __name__ == '__main__':
    cls1 = test_singleton()
    cls2 = test_singleton()
    print(cls1)
    print(cls2)
    print(cls2.show())
    cls2.add()
    print(cls1.show())
