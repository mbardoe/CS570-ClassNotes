### Python and Object Oriented Programming

Some key ideas:

* class - A class is an outline of an object. It describes the properties and methods of the objects that follow that class
* object - An object is a data structure that follows that has its own version of properties, and can run the programs 
described in the class.
* properties - pieces of data that are associated with an object (nouns/adjectives)
* methods - functions and procedures that an object can run (verbs)

#### The Point of OOP

The point of OOP is that when you are writing programs for the real world it is often helpful to be able to model the world
in the code that you write. It is helpful for us, as programmers of a robot to be able to have code that reflects that 
robot that we have. 

#### Creating classes

You create a class by using the following declaration:

```python
class My_Class:

    def __init__(self, args, more_args):
        self.property= args
        
    def my_cool_method(self, args, more_args):
        #my code
        pass
   
```
In this code, the class is called My_Class and objects made from it will be instantiations of My_Class. All the objects 
of this type would have a property named 'property', and they would all be able to use 'my_cool_method' with code like this:

```python
my_object=My_Class() # make an object of My_Class type
my_object.my_cool_method() # This makes that object do its cool method
```


#### How to import

Another very important point about OOP is that it allows abstraction. When other people make classes we only need to know
what they do (methods) and what information they track (properties). We don't necessarily need to know how the code works.
So when CTRE (Cross The Road Electronics, they make the krakens) lets us use some software they developed for their motors. 
And it has class called TalonFX. And we can look 
online, at the API (Application Programming Interface) and see that every TalonFX has a method called 
```set_speed``` that that takes a number from -1 to 1 to give a sense of 
how fast in what direction the motor runs, then getting a motor to run is as simple as:

```python
from ctre.motors import TalonFX
my_motor=TalonFX(3) # connected to the CAN Network at CAN_ID 3
my_motor.set_speed(1)
```

So to program a robot, it often isn't so much about programming or coming up with great algorithms. The first task is 
to become familiar and proficient with the libraries and classes that others have made to make the robot work.

#### __init__ method

In Python, whenever a object is instantiated.  is made it runs a special method called ```__init__```. This gives an 
opportunity for important properties to get set. When you make a class, you will most often need to make this method 
and set the appropriate properties. 

#### ```self``` keyword

The ```self``` keyword is a way for python to refer to an object before it actually exists. In a class, we don't know 
the variable name for an object because it doesn't exist yet. We use ```self``` to indicate the object that we will make 
later. Every property needs to be made using the ```self``` keyword. This makes that property have scope (it will continue to 
be available throughout the all the methods of the class) throughout all the methods of the class.


#### Practice

Let's make sure that all this makes sense. 

Choose one of these tasks depending on your level: 

* (Beginner) Open a new project and make a class file that represents a motor. Call the class ```Motor```. The motor has a 
property called ```speed```. When an object is made set the speed property to be 0.5. Write a method called ```set_speed```
that takes a number in and sets the speed property to that number. Then write a method called ```speed_up```
and another called ```slow_down```. The first method makes the motor go twice as fast, and the other one makes it go half as fast.

* (Intermediate) Create two classes. One like the one that is described above and another called a ```MotorControllerGroup```. The
```MotorControllerGroup``` should be able to have a number of motors associated to it. The MotorControllerGroup should have  
the ability to be made with a list of motors, and you should be able to use an ```add_motor``` method that takes in a motor and 
adds it to the list of motors the controller group manages. The MotorControllerGroup needs to
have a method called ```set_speed``` that takes a number and sets the speed of all the motors it controls to that speed.

* (Advanced) Investigate the difference between classmethods and staticmethods. Write a short description in your own words of
differences. Try to come up with a use case in programming the robot.

