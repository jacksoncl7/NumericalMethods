import unittest
from bisection import BisectionMethod as b

class TestBisection(unittest.TestCase):

    def test_run(self):
        '''
        representing x^2 + x - 2 in interval [-3, 0]
        it should return root -2
        '''

        root = b(1, 1, -2, [-3, 0]).run()
        self.assertEqual(root, -2)

if __name__ == '__main__':
    unittest.main()
