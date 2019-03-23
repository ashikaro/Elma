## @package elma.api.event
#  This module has the class definition for the Event class
#
#  More details.

## Events that can be emitted, watched, and responded to with event handlers.
#    Events are constructed with a jsonable value, as in
#    @code
#       Event(3.14);
#       Event("hello world");
#       Event({1,2,3});
#    @endcode
class Event:
    def __init__(self, name=None, value=0):
        self._empty = False
        self._name = name
        self._propagate = True
        self._value = value


    ## return the name of the event
    #  @param self The object pointer.
    """ """
    def name(self):
        return self._name


    ## Determine whether the event will propagate to the next event handlert
    #  @param self The object pointer.
    def propagate(self):
        return self._propagate

    ## Prevent the event from propagating to the next event handler. Typically
    # called within an event handler to prevent an subsequent events that
    # are watching the same event from firing.
    def stop_propagation(self):
        self._propagate = False

    def reset(self):
        self._propagate = True

    ## Determine whether the event has no data
    # return Whether the event has no data
    def empty(self):
        return self._empty

    ## Get the data value associated with an event
    # return The value
    def value(self):
        return self._value

