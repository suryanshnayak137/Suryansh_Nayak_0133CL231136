from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def fuel_type(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
    def fuel_type(self):
        print("Petrol")

class Bike(Vehicle):
    def start(self):
        print("Bike started")
    def stop(self):
        print("Bike stopped")
    def fuel_type(self):
        print("Petrol")

class Tesla(Vehicle):
    def start(self):
        print("Tesla started")
    def stop(self):
        print("Tesla stopped")
    def fuel_type(self):
        print("Electric")


car   = Car()
bike  = Bike()
tesla = Tesla()
print("--- Car ---")
car.start()
car.stop()
car.fuel_type()
print("\n--- Bike ---")
bike.start()
bike.stop()
bike.fuel_type()
print("\n--- Tesla ---")
tesla.start()
tesla.stop()
tesla.fuel_type()