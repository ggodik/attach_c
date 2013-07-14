import unittest
from attach_c import choose_pid

class Test( unittest.TestCase):
    def test_empty(self):
        self.assertTrue( None == choose_pid([]) )

    def test_one(self):
        self.assertTrue( 123 == choose_pid([type('PID',(),{'pid':123}),]) )

    def test_many(self):
        self.assertTrue( 123 == choose_pid([type('PID',(),{'pid':123}),
                                            type('PID',(),{'pid':456})],
                                           lambda x : '0'))

        self.assertTrue( 456 == choose_pid([type('PID',(),{'pid':123}),
                                            type('PID',(),{'pid':456})],
                                           lambda x : '1'))

    def test_cancel(self):
        self.assertTrue( None == choose_pid([type('PID',(),{'pid':123}),
                                             type('PID',(),{'pid':456})],
                                            lambda x : '-1'))        
