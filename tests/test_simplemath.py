import unittest
import simplemath as sm


class TestSimpleMath(unittest.TestCase):
    def test_add(self):
        ret = sm.add(1, 3)
        self.assertEqual(ret, 4)

    def test_negative(self):
        ret = sm.add(-1, -3)
        self.assertEqual(ret, -4)

    def test_string(self):
        ret = sm.add('a', 'b')
        self.assertEqual(ret, 'ab')

    def test_main(self):
        ret = sm.main()
        self.assertEqual(ret, None)

if __name__ == "__main__":
    unittest.main()
