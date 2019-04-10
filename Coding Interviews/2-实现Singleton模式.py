class Singleton1(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton1, cls).__new__(cls, *args, **kwargs)
        return cls._instance