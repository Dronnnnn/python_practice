"""Module that represents basic principles of OOP"""
from abc import ABC, abstractmethod


class Vehicle:
    """
    Represents a generic vehicle.

    Attributes:
        _make (str): The make of the vehicle.
        _model (str): The model of the vehicle.
    """

    def __init__(self, make, model):
        self._make = make
        self._model = model

    def get_make(self):
        """
        Get the make of the vehicle.

        Returns:
            str: The make of the vehicle.
        """
        return self._make

    def set_make(self, make):
        """
        Set the make of the vehicle.

        Args:
            make (str): The new make of the vehicle.
        """
        self._make = make

    def get_model(self):
        """
        Get the model of the vehicle.

        Returns:
            str: The model of the vehicle.
        """
        return self._model

    def set_model(self, model):
        """
        Set the model of the vehicle.

        Args:
            model (str): The new model of the vehicle.
        """
        self._model = model

    def start_engine(self):
        """
        Start the engine of the vehicle.

        Returns:
            str: A message indicating that the engine has started.
        """
        return f"Engine started in {self.get_make()} {self.get_model()}"

    def __str__(self):
        """
        Get a string representation of the vehicle.

        Returns:
            str: The make and model of the vehicle.
        """
        return f"{self._make} {self._model}"


class Car(Vehicle):
    """
    Represents a car, inheriting from the Vehicle class.

    Attributes:
        _num_people (int): The number of people the car can accommodate.
    """

    def __init__(self, make, model, num_people):
        super().__init__(make, model)
        self._num_people = num_people

    def get_num_people(self):
        """
        Get the number of people the car can accommodate.

        Returns:
            int: The number of people.
        """
        return self._num_people

    def set_num_people(self, num_people):
        """
        Set the number of people the car can accommodate.

        Args:
            num_people (int): The new number of people.
        """
        self._num_people = num_people

    def start_engine(self):
        """
        Start the engine of the car.

        Returns:
            str: A message indicating that the car engine has started.
        """
        return f"Car engine started {self.get_make()} {self.get_model()}"


class Truck(Vehicle):
    """
    A class representing a truck, inheriting from the Vehicle class.

    Attributes:
        _make (str): The make of the truck.
        _model (str): The model of the truck.
        _cargo_capacity (int): The cargo capacity of the truck in kilograms.
    """

    def __init__(self, make, model, cargo_capacity):

        super().__init__(make, model)
        self._cargo_capacity = cargo_capacity

    def get_cargo_capacity(self):
        """
        Get the cargo capacity of the truck.

        Returns:
            int: The cargo capacity of the truck in kilograms.
        """
        return self._cargo_capacity

    def set_cargo_capacity(self, cargo_capacity):
        """
        Set the cargo capacity of the truck.

        Args:
            cargo_capacity (int): The new cargo capacity of the truck in kilograms.
        """
        self._cargo_capacity = cargo_capacity

    def start_engine(self):
        """
        Start the truck's engine.

        Returns:
            str: A message indicating that the truck's engine has started.
        """
        return f"Truck engine started {self.get_make()} {self.get_model()}"


class Motorcycle(Vehicle):
    """
    A class representing a motorcycle, inheriting from the Vehicle class.

    Attributes:
        _make (str): The make of the motorcycle.
        _model (str): The model of the motorcycle.
        _type_motorcycle (str): The type of the motorcycle (e.g., Cruiser, Sport).
    """

    def __init__(self, make, model, type_motorcycle):

        super().__init__(make, model)
        self._type_motorcycle = type_motorcycle

    def get_type_motorcycle(self):
        """
        Get the type of the motorcycle.

        Returns:
            str: The type of the motorcycle.
        """
        return self._type_motorcycle

    def set_type_motorcycle(self, type_motorcycle):
        """
        Set the type of the motorcycle.

        Args:
            type_motorcycle (str): The new type of the motorcycle.
        """
        self._type_motorcycle = type_motorcycle

    def start_engine(self):
        """
        Start the motorcycle's engine.

        Returns:
            str: A message indicating that the motorcycle's engine has started.
        """
        return f"Motorcycle engine started {self.get_make()} {self.get_model()}"


class Shape(ABC):
    """
    An abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    A class representing a circle, inheriting from the Shape class.

    Attributes:
        _radius (float): The radius of the circle.
    """

    def __init__(self, radius):

        self._radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return 3.14 * self._radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * 3.14 * self._radius


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from the Shape class.

    Attributes:
        _width (float): The width of the rectangle.
        _height (float): The height of the rectangle.
    """

    def __init__(self, width, height):

        self._width = width
        self._height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self._width + self._height)


if __name__ == "__main__":

    car = Car("Toyota", "Corolla", 4)
    car.set_make("BMW")
    print(car.get_make())

    motorcycle = Motorcycle("Harley-Davidson", "Street 750", "Cruiser")
    print(motorcycle)
