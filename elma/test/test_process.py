from elma.api.process import Process
from elma.api.event import Event
## @package elma.test.test_process
#  This module contains the class definition for TestProcess.

## This is a test process class inheriting the Process class
#  to test the working of the ELMA process APIs.
class TestProcess(Process):

    def __init__(self, name=None, status=None, manager=None):
        super().__init__(name)

    def hello(self, e):
        self.str = e.value()

    def pi(self, e):
        self.x = e.value()

    def init(self):

        self.watch("hello", self.hello )

        self.watch("pi", self.pi)

    def start(self):
        print("empty start implementation in the TestProcess")

    def update(self):
        print("emitting hello event\n")
        self.emit(Event("hello", "world"))
        print("emitting pi event\n")

        self.emit(Event("pi", 3.14))

    def stop(self):
        print("empty stop implementation in the TestProcess")




