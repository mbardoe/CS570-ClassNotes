[comment]: render
# Day 04
## Object-Oriented Programming and Classes
### Classes

#### What is a class?

A class is a blueprint for creating objects (a particular data structure), providing initial values for state (member 
variables or attributes), and implementations of behavior (member functions or methods).
So class is the general scheme for the object, and the object is the specific instance of the class.

#### Why use classes?

Classes allow us to create objects that have their own properties and methods. This allows us to create objects 
that are more complex than simple data structures.

#### How to create a class

In python, we create a class by using the keyword `class` followed by the name of the class. The class definition
is followed by a colon and the body of the class is indented. Let's take a look at an example from the 2025 robot
code:

```python

import ntcore
from wpilib import DigitalInput

import config
import constants
from toolkit.motors.ctre_motors import TalonFX
from toolkit.subsystem import Subsystem
from units.SI import meters, meters_to_inches


class Elevator(Subsystem):
    def __init__(self):
        super().__init__()
        self.leader_motor: TalonFX = TalonFX(
            config.elevator_lead_id,
            config.foc_active,
            inverted=False,
            config=config.ELEVATOR_CONFIG
        )
        self.follower_motor: TalonFX = TalonFX(
            config.elevator_follower_id,
            config.foc_active,
            inverted=False,
            config=config.ELEVATOR_CONFIG
        )

        self.target_height: meters = 0.0
        self.elevator_moving: bool = False

    def init(self):
        self.leader_motor.init()
        self.follower_motor.init()
        self.follower_motor.follow(self.leader_motor, inverted=True)
        self.leader_motor.set_sensor_position(0)

    @staticmethod
    def limit_height(height: meters) -> meters:
        """
        limits the height of the elevator to both a max and min
        """
        if height > constants.elevator_max_height:
            return constants.elevator_max_height
        elif height < 0.0:
            return 0.0
        return height

    def set_position(self, height: meters) -> None:
        """
        Brings the elevator to given height

        Args:
            height (meters): intended elevator height in meters
        """
        height = self.limit_height(height)
        self.target_height = height

        rotations = (
            height * constants.elevator_gear_ratio
        ) / constants.elevator_driver_gear_circumference
        self.leader_motor.set_target_position(rotations)

    def stop(self) -> None:
        """
        Stops the elevator
        """
        self.set_position(self.get_position())

    def set_zero(self) -> None:
        """
        Brings the elevator to the zero position
        """
        self.set_position(0)

    def get_position(self) -> meters:
        """
        Obtains the current height of the elevator

        Returns:
            return_float: current elevator height in meters
        """
        return (
            self.leader_motor.get_sensor_position()
            * constants.elevator_driver_gear_circumference
            / constants.elevator_gear_ratio
        )

    def is_at_position(self, height: meters) -> bool:
        """
        checks if the elevator is at a certain height

        Args:
            height (meters): height to be checked
        """
        return abs(self.get_position() - height) < config.elevator_height_threshold

    def update_table(self) -> None:
        table = ntcore.NetworkTableInstance.getDefault().getTable("Elevator")

        table.putNumber("height", self.get_position() * meters_to_inches)
        table.putNumber("target height", self.target_height * meters_to_inches)
        table.putNumber(
            "motor lead applied output", self.leader_motor.get_applied_output()
        )
        table.putNumber(
            "motor lead current", self.leader_motor.get_motor_current()
        )
        table.putNumber(
            "motor follow applied output", self.follower_motor.get_applied_output()
        )

    def periodic(self):
        if config.NT_ELEVATOR:
            self.update_table()

```

Some things about this code that I want you to notice:

* The class is defined with the keyword `class` followed by the name of the class.
* The class definition is followed by a colon and the body of the class is indented.
* The class has a method called `__init__` which is a special method that is called when an object is created from the class.
* The class has other methods that define the behavior of the class.
* The class has properties that define the state of the class.
* Next to the name of the class is a set of parentheses that say what class this class inherits from. 
In this case, the class inherits from `Subsystem` which is a class that we made to help organize the robot code.


#### How to create an object from a class

To create an object from a class, we use the class name followed by a set of parentheses. Let's take a look at an example:

```python
elevator = Elevator()
```
If the robot had multiple elevators we could make multiple objects from the class like this:

```python
elevator_1 = Elevator()
elevator_2 = Elevator()
```

#### How to access properties and methods of an object

To access the properties and methods of an object, we use the dot operator. Let's take a look at an example:

```python
elevator.set_height(0.8)
```

In this example, we are calling the `set_height` method of the `elevator` object and passing in the value `0.8`.

```python
height = elevator.get_position()
```

In this example, we are calling the `get_position` method of the `elevator` object and storing the return value in the variable `height`.

```python
if elevator.is_at_position:
    print("Reached the proper height")
```

In this example, we are accessing the `is_at_position` property of the `elevator` object and checking if it is `True`.

#### Summary

In this lesson, we learned about classes in python. We learned what a class is, why we use classes, how to create a 
class, how to create an object from a class, and how to access properties and methods of an object. Classes are a 
powerful tool in python that allow us to create objects that have their own properties and methods. We will be using 
classes extensively in our robot code to organize and structure our code.


#### Practice

Let's make sure that all this makes sense.

1. What is a class?


2. Why use classes?


3. How do you create a class in python?



4. How do you create an object from a class?


5.  How do you access properties and methods of an object?



6. What is the `__init__` method and what does it do?



#### Practical Practice

Start the assignment at [https://classroom.github.com/a/utnqGH_3](https://classroom.github.com/a/utnqGH_3)

#### Notes on Data Structures in Python

Python has the following data structures:

* Lists - which are made using square brackets `[]`
* Tuples - which are made using parentheses `()`. Tuples are immutable, meaning that once they are created, they cannot be changed.
* Sets - which are made using curly braces `{}`. Sets are unordered collections of unique elements.
* Dictionaries - which are made using curly braces `{}`. Dictionaries are collections of key-value pairs.
* Strings - which are made using single or double quotes `''` or `""`.
* Numbers - which can be integers or floats.
* Booleans - which can be `True` or `False`.
* None - which is a special type that represents the absence of a value.
* Objects - which are instances of classes.
* Functions - which are objects that can be called.
