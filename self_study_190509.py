class MyMap(object):
    def __init__(self, func, *iterables):
        pass

    def __getattribute__(self, name, *args, **kwargs):
        return getattr(self, name)

    def __iter__(self, *args, kwargs):
        pass

    @staticmethod
    def __new__(*args, **kwages):
        pass

    def __next__(self, *args, kwargs):
        pass

    def __reduce__(self, *args, **kwargs):
        pass


a = [1.4, 4.3, 8.5, 9.8]

# mymap = MyMap()

b = list(MyMap(int, a))
print(b)
