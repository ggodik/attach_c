import unittest
from attach_c import get_processes
import getpass

class Test( unittest.TestCase):
    def test_list_for_self(self):
        user = getpass.getuser()
        procs = get_processes(user,"python")
        self.assertTrue(len(procs)>0)
