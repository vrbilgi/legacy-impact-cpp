import unittest
from Class import *


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        c = classname()
        c.append("NinethBox : public Shape ,Shape2")
        length = len(c.listClasses)
        self.assertEqual(1,length)


if __name__ == '__main__':
    unittest.main()
