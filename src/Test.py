import unittest
from readFile import *
class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_1(self):
        readFolder("TestFiles")
    #    self.assertEquals(res,Output)

if __name__ == '__main__':
    unittest.main()
