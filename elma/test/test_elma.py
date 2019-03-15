import unittest
from elma.api.process import Process
from elma.api.manager import Manager
from elma.api.event import Event
from elma.test.test_process import TestProcess

class TestElma(unittest.TestCase):


   def test_process(self):
      p = TestProcess("P")
      m = Manager()
      m.schedule(p, 10)
      m.init()
      p.update()
      self.assertEqual("world", p.str)
      self.assertEqual(3.14, p.x)




if __name__ == "__main___":
    unittest.main()
