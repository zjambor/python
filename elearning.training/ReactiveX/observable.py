import abc
from observer import Observer

class Observable(abc.ABC):
    def __init__(self):
        self.observers = set()
        self.complete = False

    def subscribe(self, subscriber):
        if not isinstance(subscriber, Observer):
            raise ValueError('Only Observer objects are valid subscribers.')
        self.observers.add(subscriber)

    def _event(self, event):
        if self.complete:
            raise RuntimeError("Can't send events on a completed Observable.")
        for obs in self.observers:
            obs.on_event(event)

    def _exception(self, exception):
        if self.complete:
            raise RuntimeError("Can't send exceptions on a completed Observable.")
        for obs in self.observers:
            obs.on_exception(exception)

    def _complete(self):
        if self.complete:
            raise RuntimeError("Can't complete an already completed Observable.")
        self.complete = True
        for obs in self.observers:
            obs.on_complete()
            