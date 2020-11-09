'''
file in which we test the square
'''

import unittest

from smartsquare.core import square

class TestCore(unittest.TestCase):
    '''class in which there is the test'''
    def test_float(self):
        '''function in which file does the test the float'''
        self.assertAlmostEqual(square(2.), 4.)


if __name__ == '__main__':
    unittest.main()
