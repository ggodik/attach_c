import unittest

class Test( unittest.TestCase):
    def setUp(self): pass
    def tearDown(self): pass

    def test_instantiate(self):
        from attach_c.command import Attach_C
        ac = Attach_C()
