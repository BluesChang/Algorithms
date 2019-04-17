'''
题目：设计一个类，我们只能生成该类的一个实例
'''


# 通过_new_方法实现单例
class Singleton1(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton1, cls).__new__(cls, *args, **kwargs)
        return cls._instance


# 通过Decorator实现
from functools import wraps


def SingleTon2(cls):
    _instance = {}

    @wraps(cls)
    def single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return single


@SingleTon2
class SingleTon(object):
    def __init__(self, text):
        self.text = text


# 通过import实现
# singleton.py
class SingleTon3(object):
    def __init__(self, text):
        self.text = text


single = SingleTon3('singleton')
# test.py
from singleton import SingleTon3
