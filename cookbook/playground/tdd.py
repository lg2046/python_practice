from .my_dict import MyDict

import unittest


class DictTest(unittest.TestCase):

    # 在当前TestCase的整个测试开始前与开始后, 即当前类只会运行一次
    def setUp(self):
        print("test if start")

    def tearDown(self):
        print("test if over")

    def test_init(self):
        d = MyDict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_raise(self):
        d = MyDict(a=1, b='test')

        with self.assertRaises(KeyError):
            value = d['empty']
