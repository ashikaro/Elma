class Transition:
    def __init__(self, event_name, from_state, to_state):
        self._from_state = from_state
        self._to_state = to_state
        self._event_name = event_name

    def from_state(self):
        return self._from_state

    def to_state(self):
        return self._to_state

    def event_name(self):
        return self._event_name
