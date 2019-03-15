class Event:
    def __init__(self, name=None, value=0):
        self._empty = False
        self._name = name
        self._propagate = True
        self._value = value

    def name(self):
        return self._name

    def propagate(self):
        return self._propagate

    def stop_propagation(self):
        self._propagate = False

    def reset(self):
        self._propagate = True

    def empty(self):
        return self._empty

    def value(self):
        return self._value

