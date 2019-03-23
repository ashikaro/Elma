import unittest
from elma.api.manager import Manager
from elma.api.event import Event
from elma.test.test_process import TestProcess
from elma.api.robot import Robot

class TestElma(unittest.TestCase):

   def test_process(self):
      print("Running tests for core ELMA APIs Using ELMA Manager to test: "
            "1. Initializing a process "
            "2. Scheduling a process  "
            "3. Updating a process "
            "4. Event handler methods watch and emit")
      p = TestProcess("P")
      m = Manager()
      m.schedule(p, 10)
      m.init()
      p.update()
      self.assertEqual("world", p.str)
      self.assertEqual(3.14, p.x)

   def test_robot(self):
      print("Running first set of tests for python client Robot Leveraging ELMA APIs.")

      test_robo = Robot("What a very nice robot")
      m = Manager()
      m.schedule(test_robo,10)
      m.init()
      m.start()

      wander = "Wander"
      noise = "Make Noise"
      evade = "Evade"

      # Send signals to robot and test

      m.emit(Event("start"))
      print(test_robo.current().name())
      self.assertEqual(test_robo.current().name(),wander)

      print("emitting event intruder detected")
      m.emit(Event("intruder detected"))
      print(test_robo.current().name())
      self.assertEqual(test_robo.current().name(),noise)

      m.emit(Event("proximity warning"))
      print(test_robo.current().name())
      self.assertEqual(test_robo.current().name(),evade)

      m.emit(Event("battery full"))
      print(test_robo.current().name())
      self.assertEqual(test_robo.current().name(),evade)

   def test_robot_two(self):
      print("Running First set tests for python client Robot Leveraging ELMA APIs.")

      test_robo = Robot()
      m = Manager()
      m.schedule(test_robo,10)
      m.init()
      m.start()

      wander = "Wander"
      noise = "Make Noise"
      evade = "Evade"
      find_recharge = "Find Recharge Station"
      recharge = "Recharge"

      # Send signals to robot and test
      print(test_robo.current().name())
      self.assertEqual(test_robo.current().name(), wander)

      print("emitting event battery low")
      m.emit(Event("battery low"))
      print(test_robo.current().name())
      self.assertEqual(test_robo.current().name(), find_recharge)

      m.emit(Event("found recharge station"))
      print(test_robo.current().name())
      self.assertEqual(test_robo.current().name(), recharge)

      m.emit(Event("battery full"));
      print(test_robo.current().name())
      self.assertEqual(test_robo.current().name(), wander)

      m.emit(Event("intruder detected"))
      print(test_robo.current().name())
      self.assertEqual(test_robo.current().name(), noise)

      m.emit(Event("reset"))
      print(test_robo.current().name())
      self.assertEqual(test_robo.current().name(), wander)

      m.emit(Event("intruder detected"))
      print(test_robo.current().name())
      self.assertEqual(test_robo.current().name(), noise)

      m.emit(Event("proximity warning"))
      print(test_robo.current().name())
      self.assertEqual(test_robo.current().name(), evade)

      m.emit(Event("battery low"))
      print(test_robo.current().name())
      self.assertEqual(test_robo.current().name(), find_recharge)


if __name__ == "__main___":
    unittest.main()
