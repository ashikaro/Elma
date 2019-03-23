## A class which represents a State in the Finite State Machine.

class State:

    _id_counter = 0

    def __init__(self, name="unnamed state"):
        self._name = name
        self._state_machine = None
        self._id = State._id_counter
        State._id_counter = State._id_counter + 1
        print("Id for state {} is {}".format(self.name(),self._id))

    def _emit(self, event):
         if self._state_machine is None:
             raise Exception("Cannot access events in a state before the is added to a state machine.")
         else:
             self._state_machine.emit(event)

    ## \return The name of the state
    def name(self):
        return self._name

    ## \return The id of the state
    def id(self):
        return self._id

    ## A method that derived instances should define. It is called when the state is
    # entered by the state machine either when the machine starts or when a transition
    # to the state is fired.
    # \param e The event that led to the transition into the state
    def entry(self, event):
        raise NotImplementedError("Must override entry in derived classes")

    ## A method that derived instances should define. It is called repeatedly by the
    # update() method of the containing StateMachine when the state is active.
    def during(self, event):
        raise NotImplementedError("Must override during in derived classes")

    ## A method that derived instances should define. It is called just before the state is
    # exited by the state machine when a transition
    # from the state is fired.
    # \param e The event that led to the transition out of the state
    def exit(self, event):
        raise NotImplementedError("Must override exit in derived classes")






