from abc import ABC, abstractmethod


class Engine:
    pass


class AbstractObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class ObservableEngine(Engine):
    pass


class ShortNotificationPrinter(AbstractObserver):
    def update(self):
        pass


class FullNotificationPrinter(AbstractObserver):
    def update(self):
        pass