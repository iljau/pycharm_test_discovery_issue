import unittest


class SomeTestCase(unittest.TestCase):
    def test01_success(self):
        assert True

    def test02_fail(self):
        assert False