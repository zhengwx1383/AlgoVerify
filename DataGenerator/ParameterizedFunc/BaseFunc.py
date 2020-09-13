import numpy as np

class BaseFunc:
    def __init__(self, **args):
        self.params = args

    def calc(self, x):
        '''
            called by user. calling `self.call` in the end, which is written by subclass
            @x anything convertable for numpy.array
        '''
        x = np.array(x, dtype=np.float)
        if len(x.shape) > 1:
            raise ValueError('length of shape of `np.array(x)` is greater than 1')
        x = x.reshape([-1])
        if x.size == 0:
            return np.array(list())
        return self.call(x) # subclass call

    def call(self, x):
        raise NotImplementedError()

    def getParameter(self, key, default=0.0, dtypes=(int, float)):
        '''
            supporting function. used in `__init__` of subclass.
            get parameters from self.params and then validate it.
            @key name of parameter
            @default default value.
            @dtypes valid data type
        '''
        value = default
        if key in self.params:
            value = self.params[key]
            if not isinstance(value, dtypes):
                raise ValueError('type of %s is not in %s' % (str(key), str(dtypes)))
        return value