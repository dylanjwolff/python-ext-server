import unittest
import server

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        self.assertEqual(2, server.exampleFn(1,1))

if __name__ == '__main__':
    unittest.main()
