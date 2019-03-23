from enum import Enum
from datetime import timedelta, datetime
from time import time
from abc import ABCMeta, abstractmethod


class Status_Type(Enum):
    UNINITIALIZED = 1
    STOPPED = 2
    RUNNING = 3

## abstract base class
class Process:
    __metaclass__ = ABCMeta

    ## Status of the process, as managed by a Manager. Get the
    # status using the status() getter.
    def __init__(self, name=None, status=None, manager=None):
        if name is None:
            self._name = "unnamed process"
        else:
            self._name = name

        if status is None:
            self._status = Status_Type.UNINITIALIZED
        else:
            self._status = status

        if manager is None:
            self._manager = None
        else:
            self._manager = manager
        self._last_update = timedelta(0)
        self._previous_update = timedelta(0)

    @abstractmethod
    def init(self):
        # implement init method
        raise NotImplementedError("Must override init in derived classes")

    @abstractmethod
    def start(self):
        raise NotImplementedError("Must override start in derived classes")

    @abstractmethod
    def update(self):
        raise NotImplementedError("Must override update in derived classes")

    @abstractmethod
    def stop(self):
        raise NotImplementedError("Must override stop in derived classes")

    ## Getter
    # \return The period of the process.
    def period(self):
        return self._period

    ## Getter
    # \return The status of the process.
    def status(self):
        return self._status

    ## Getter
    # \return The name of the process.
    def name(self):
        return self._name

    ## Getter
    # \return The number of updates since the process was last started by the Manager.
    def num_updates(self):
        return self._num_updates

    ## Getter
    # \return The time the process was last started by the Manager.
    def start_time(self):
        return self._start_time

    ## Getter
    # \return The duration of time between the start time and the most recent
    # time the Manager called the update() method.
    def last_update(self):
        return self._last_update

    ## Getter
    # \return The duration of time between the start time and the second most recent
    # time the Manager called the update() method.
    def previous_update(self):
        return self._previous_update

    ## The time since the last update in millisconds, as a double
    #
    # return The time since the last update, in milliseconds
    #
    def milli_time(self):
        return self.last_update()

    def diff_count(self):
        self.diff_count = self.last_update() - self.previous_update()
        return self.diff_count

    def watch(self, event_name, handler):
        print("watching for {}".format(event_name))
        if self._manager is None:
            raise Exception('Cannot access events in a process before the process is scheduled')
        else:
            self._manager.watch(event_name, handler)

    def emit(self, event):
        print("emitting event {}".format(event.name()))
        if self._manager is None:
            raise Exception('Cannot access events in a process before the process is scheduled')
        else:
            self._manager.emit(event)

    # Manager interface

    def _init(self):
        self._status = Status_Type.STOPPED
        self.init()

    ## Manager interface for the _start method. Do not call directly.
    def _start(self, elapsed):
        self._status = Status_Type.RUNNING
        self._start_time = datetime.now()
        self._last_update = elapsed
        self._num_updates = 0
        self.start()

    ## Manager interface for the _update method. Do not call directly.
    def _update(self, elapsed):
        print('in process_update elapsed: {}'.format(elapsed))
        self._previous_update = self._last_update;
        self._last_update = elapsed
        self.update()
        ++self._num_updates

    ## Manager interface for the _stop method. Do not call directly.
    def _stop(self):
        self._status = Status_Type.STOPPED
        self.stop()


