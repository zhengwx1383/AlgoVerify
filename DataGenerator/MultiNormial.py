import numpy as np
from collections import abc

from .ParameterizedFunc.PositiveSine import PositiveSine
from .ParameterizedFunc.BaseFunc import BaseFunc

class MultiNormial:
    def __init__(self, ndim, config=None):
        config = self.defaultConfig(ndim)

    @staticmethod
    def defaultConfig(ndim):
        def randomSineConfig():
            c = dict()
            c['A'] = np.random.rand() * 3 + 0.2
            c['Phi'] = np.random.rand() * 2 * np.pi
            return c
        out = list()
        for _ in range(0, ndim):
            c = randomSineConfig()
            out.append((PositiveSine, c))
        return out

    @staticmethod
    def checkConfig(config):
        if not isinstance(config, abc.Iterable):
            return False, 'config is not `abc.Iterable` (such as list, tuple)'
        if len(config) == 0:
            return False, 'length of config is 0'
        for c in config:
            if not isinstance(c, abc.Iterable):
                return False, 'elements of config is not `abc.Iterable` (such as list, tuple)'
            if len(c) != 2:
                return False, 'elements of config is not (dict, BaseFunc)'
            target_class, params = c
            if type(target_class) != type:
                return False, 'config[*][0] is not a class.'
            if not issubclass(target_class, BaseFunc):
                return False, 'config[*][0] is not subclass of BaseFuc'
            if not isinstance(params, dict):
                return False, 'config[*][1] is not a dict'
        return True, 'OK'
