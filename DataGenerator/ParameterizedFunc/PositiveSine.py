import numpy as np
from .BaseFunc import BaseFunc

class PositiveSine(BaseFunc):
    '''
        @A amplitude of sine function
        @Phi phase shift of sine function
    '''
    def call(self, x):
        '''
            called by `BaseFunc.calc`
            @x numpy.ndarray: [x1, x2, ..., xn]
            @return numpy.ndarray: [f(x1), f(x2), f(x3), ..., f(xn)]
        '''
        A = self.getParameter('A', default=1.0)
        Phi = self.getParameter('Phi')
        return np.sin(x + Phi) * A + 0.5 * A
