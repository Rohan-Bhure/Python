# abstraction -> Hiding complexity and showing only essential things
# Hiding unnecessary details showing important
# programing meaning -> user knows how to use not known how to implement

from abc import ABC, abstractmethod

# cannot create the object of abstract class 
# we can define constrctor as well
# abstract class has normal methods
# flexible system, complex architeture easier 
class Animal(ABC):
    @abstractmethod # use to create commplsary method
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog sound")

class Cat(Animal):
    def sound(self):
        return super().sound()

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Notifier class

class Notifier(ABC):
    @abstractmethod
    def send(message, receiver):
        pass

    @abstractmethod
    def schedule(message, receiver, time):
        pass

    @abstractmethod
    def validate_receiver(receiver):
        pass
    

class EmailNotifier(Notifier):
    def __init__(self):
        self.sent_emails = []
        self.schedule_emails = []
    def send(message, receiver):

        

    def schedule(message, receiver, time):
        

    def validate_receiver(receiver):
        if receiver.endswith("@gmail.com") and len(receiver) >= 11 :
            return True
        else:
            return False

class SMSNotifier(Notifier):
    def send(message, receiver):
        pass

    def schedule(message, receiver, time):
        pass

    def validate_receiver(receiver):
        pass

class PushNotifier(Notifier):
    def send(message, receiver):
        pass

    def schedule(message, receiver, time):
        pass

    def validate_receiver(receiver):
        pass

class WhatsAppNotifier(Notifier):
    def send(message, receiver):
        pass

    def schedule(message, receiver, time):
        pass

    def validate_receiver(receiver):
        pass


# Notification Service Class

class NotificationService:
    Notifier 