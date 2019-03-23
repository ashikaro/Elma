from elma.api.process import Process
from elma.api.transition import Transition
from elma.api.event import Event


class StateMachine(Process):
    def __init__(self, name="unnamed state machine"):
        super().__init__(name)
        self._initial = None
        self._current = None
        self._propagate = False
        self._transitions = []

    def set_initial(self, s):
        self._initial = s

    def add_transition(self, event_name, from_state, to_state):
        print('adding transition for event {} from {} to {}'.format(event_name, from_state.name(),to_state.name()))
        self._transitions.append(Transition(event_name, from_state, to_state))
        to_state._state_machine = self
        from_state._state_machine = self

    def init(self):
        for transition in self._transitions:
            def gen_event_handler(transition):
                def handler(e):
                    if(self._current.id() == transition.from_state().id()):
                        self._current.exit(e)
                        self._current = transition.to_state()
                        self._current.entry(e)
                        if(self._propagate==False):
                            e.stop_propagation()
                return handler

            cur_event_handler = gen_event_handler(transition)
            self.watch(transition.event_name(), cur_event_handler)


    def start(self):
        if self._initial is None:
            raise Exception("State machine started without an initial state. Call set_initial() first")

        self._current = self._initial
        self._current.entry(Event("start"))

    def stop(self):
        print("empty implementation overriding base class\n")

    def update(self):
        self._current.during()

    def set_propagate(self, val):
        self._propagate = val

    def current(self):
        return self._current



