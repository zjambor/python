import abc

class Observer(abc.ABC):
    """
    abc = Abstract Base Class
    """
    @abc.abstractmethod
    def on_event(self, event):
        pass

    def on_exception(self, exception):
        pass

    def on_complete(self):
        pass

