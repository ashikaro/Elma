from datetime import datetime, timedelta

class State:
    def _emit(self, event):
         if self._state_machine is None:
             raise Exception("Cannot access events in a state before the is added to a state machine.")
         else:
             self._state_machine.emit(event)





