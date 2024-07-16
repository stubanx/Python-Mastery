# Day 34

### What is Data Abstraction?
Data abstraction is all about **hiding complex implementation details** while exposing only essential information and functionalities to users. Imagine you're driving a car: you know how to accelerate, brake, and steer, but you don't need to understand the intricate workings of the engine or transmission. That's data abstraction in action!

### Basic Concepts:
1. **Classes in Python**: Classes define the blueprint for creating objects. They encapsulate data (attributes) and behavior (methods). For example, a `Car` class might have attributes like `make`, `model`, and methods like `start_engine()` and `stop_engine()`¹.

2. **Abstract Classes**: An abstract class is a class that contains one or more **abstract methods**. These methods are declared without implementation. Abstract classes serve as templates for other classes. In Python, we create abstract classes using the `abc` (abstract base class) module. An abstract class ensures that its child classes provide implementations for its abstract methods.

3. **Abstract Methods**: These are methods declared in an abstract class but not implemented there. They act as placeholders, defining what methods a subclass must implement. For instance, consider this abstract class:

    ```python
    from abc import ABC, abstractmethod

    class Vehicle(ABC):
        @abstractmethod
        def start(self):
            pass

        @abstractmethod
        def stop(self):
            pass
    ```

    Here, `start()` and `stop()` are abstract methods. Any class inheriting from `Vehicle` must provide concrete implementations for these methods.

### Real-Life Example:
Let's create a simple example with a `Shape` class. We'll define an abstract method called `area()` that calculates the area of different shapes. Subclasses (like `Circle` and `Rectangle`) will implement this method.

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Usage
circle = Circle(radius=5)
rectangle = Rectangle(length=4, width=3)

print(f"Circle area: {circle.area()}")
print(f"Rectangle area: {rectangle.area()}")
```

In this example, we've abstracted the concept of a shape's area. Users of the `Circle` and `Rectangle` classes don't need to know the internal details—they can simply call `area()` to get the result.

Remember, data abstraction promotes code organization, reusability, and maintainability. It's like driving a car without worrying about the engine internals—just focus on the essential actions! 🚗🔍¹².