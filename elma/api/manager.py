from datetime import datetime, timedelta

    #! The Process Manager class.
class Manager:
    def __init__(self):
        self.event_handlers = dict()
        self._processes = []
        self._elapsed = timedelta(0)

    def schedule(self, process, period):
        process._period = timedelta(seconds=period)
        self._processes.append(process)
        process._manager = self


    #! Getter
    #! \return The time the Manager was most recently started
    def start_time(self):
        return self._start_time

    #! Getter
    #! \return The  duration of time since the manager was most recently started
    def elapsed(self):
        return self._elapsed

    # Event Interface
    def watch(self, event_name, handler):
        if event_name in self.event_handlers:
            handlers = self.event_handlers[event_name]
        else:
            handlers = []

        handlers.append(handler)
        self.event_handlers[event_name] = handlers


    #! Emit an event associated with a name.
    #! Typically, a process would emit events in its update() method using something like
    #! the following code"
    #! @code
    #!     emit(Event("name", value));
    #! @endcode
    #! where value is any jsonable value. For example, you can write
    #! @code
    #!     emit(Event("velocity", 3.41));
    #! @endcode
    #! \param event The Event to be emitted
    #! \return A reference to the manager for chaining.
    def emit(self, event):
        e = event
        print('emitting event {}'.format(event.name()))
        if event.name()  in self.event_handlers:
            for handler in self.event_handlers[event.name()]:
                if e.propagate():
                    handler(e)

    #! Apply a function to all processes.
    #! \param f The function to apply. It should take a reference to a process and return void.
    #! \return A reference to the manager, for chaining
    def all(self, f):
        for process in self._processes:
            print(process)
            f(process)

    #! Initialize all processes. Usually called before run()
    #! \return A reference to the manager, for chaining
    def init(self):
        func = lambda p: p._init()
        self.all(func)

    #! Start all processes. Usually not called directly.
    #! \return A reference to the manager, for chaining
    def start(self):
        func = lambda p: p._start(self._elapsed)
        self.all(func)

    #! Stop all processes. Usually not called directly.
    #! \return A reference to the manager, for chaining
    def stop(self):
        func = lambda p: p._stop(self._elapsed)
        self.all(func)

    #! Update all processes if enough time has passed. Usually not called directly.
    #! \return A reference to the manager, for chaining
    def update(self):
        self.all(self._update)

    #! Update all processes if enough time has passed. Usually not called directly.
    #! \return A reference to the manager, for chaining
    def _update(self, p):

        if self._elapsed > (p.last_update() + p.period()):
            p._update(self._elapsed)

    #! Run the manager for the specified amount of time.
    #! \param The desired amount of time to run
    #! \return A reference to the manager, for chaining
    def run(self, runtime):
        self._start_time = datetime.now()
        self._elapsed = timedelta(0)
        self.start()

        while(self._elapsed < runtime):
            self.update()
            self._elapsed =  self.get_milliseconds(datetime.now() - self._start_time)

        self.stop()

    def get_milliseconds(self, duration):
        return duration.total_seconds() * 1000



