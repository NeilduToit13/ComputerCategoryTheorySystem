import unittest
from object import object

class TestObject(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.A = object('A')

    def tearDown(self):
        pass

    def test_object(self):
        result = str(self.A)
        self.assertEqual(result, 'A')

if __name__=="__main__":
    unittest.main()
