from datetime import datetime, timedelta

class Manager:
    def __init__(self):
        self.event_handlers = dict()
        self._processes = []
        self._elapsed = timedelta(0)

    def schedule(self, process, period):
        process._period = timedelta(seconds=period)
        self._processes.append(process)
        process._manager = self

    def start_time(self):
        return self._start_time

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

    def emit(self, event):
        e = event
        if event.name() in self.event_handlers:
            for handler in self.event_handlers[event.name()]:
                if e.propagate():
                    handler(e)

    def all(self, f):
        for process in self._processes:
            print("loop over all processes\n")
            print(process)
            f(process)

    def init(self):
        func = lambda p: p._init()
        self.all(func)

    def start(self):
        func = lambda p: p._start(p._elapsed)
        self.all(func)

    def stop(self):
        func = lambda p: p._stop(p._elapsed)
        self.all(func)

    def update(self):
        self.all(self._update)

    def _update(self, p):
        print('in lambda')
        print('elapsed: {}'.format(self._elapsed))
        print('compared with : {}'.format(p.last_update() + p.period()))

        if self._elapsed > (p.last_update() + p.period()):
            print('calling processes update method')
            p._update(self._elapsed)

    def run(self, runtime):
        print('In manager run')
        self._start_time = datetime.now()
        self._elapsed = timedelta(0)
        self.start()

        while(self._elapsed < runtime):
            print("calling processes update\n in manager")
            self.update()
            self._elapsed =  self.get_milliseconds(datetime.now() - self._start_time)

        self.stop()

    def get_milliseconds(self, duration):
        return duration.total_seconds() * 1000



