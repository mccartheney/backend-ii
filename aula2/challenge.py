# Challenge Session 2: Observer Pattern
# Problem: Implement the Observer pattern to notify multiple observers when a subject’s state changes.

class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received: {message}")

class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

    def set_state(self, state):
        self._state = state
        self.notify(f"State changed to {state}")

if __name__ == "__main__":
    subject = Subject()
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")
    subject.attach(observer1)
    subject.attach(observer2)
    subject.set_state("ACTIVE")
    subject.set_state("INACTIVE")
