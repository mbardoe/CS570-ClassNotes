[comment]: render
# Day 6 CS570
## Test Review on Git/GitHub/OOP/TimedRobot


1. Describe the purpose of a *branch* in git. What is the goal of a *main* branch?


\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

2. Write code for a claw object. The claw should have methods that allow it to open and close. The Claw object should have 
a dunder init that should create a motor that the claw uses in its methods. Imagine that motor has a method called ```set_speed``` that
takes in a number between -1 and 1 to indicate how fast and in what direction to run the motor.


\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 




3. A friend of your writes code to run your robot. They have put that code in a file called ```drivingwell.py```. Inside the
file is a class called ```DriveRobot```. The ```DriveRobot``` class has an ```__init__``` method that requires two numbers 
the first is the width of the robot in centimeters, and the second is the length of the robot in centimeters. Your robot
is 55 cm wide and 60 cm long. What two lines of code are you going to add to your ```robot.py``` file to utilize your friends
code after you have imported his file into the same directory as your ```robot.py``` file. 


\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 





4. Ximena is making some changes to their robot code. They are currently on the ```dev/shooter``` branch of their git project 
that they are working on with other students. They have made significant changes, and have had an opportunity to test those
changes on the robot and things seem to be working well. What should they do next to share their changes with other members
of their team.

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

5. A team is considering several different types arms to score game pieces in their competition. The team decides to move
forward with designing and coding two different arms. Describe how object oriented 
programming can support the development of two different kinds of arms. The programming lead wants to make it so that 
the code from either team can be utilized with the rest of the code. Describe how object oriented ideas can be used to make this type of development possible.

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

8. Write a class ```Turret``` class in python with following requirements.

    * The turret class initializers takes in two arguments the first is the CAN of id of the motor that runs the turret,
      the second is a id number for the DIO port that the sensor is connected to.
    * Instantiate a ```Motor``` class using as an input of of the CAN id that was given in the intialization.
    * Instantiate a ```Sensor``` using as an input the id that was given in the intialization.
    * The class has a ```turn``` method that takes in a number between -1 and 1 and uses the ```Motor```'s ```setspeed```
      method to set the speed of the turret.
    * The class has a ```get_position``` method that uses the ```Sensor```'s ```get_value``` method to report the position
      of the turret.
    * Import the ```Motor``` and ```Sensor``` from ```wpilib```
    * Make it possible to print the ```Turret``` class to the console and report the speed and position of the robot.

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 



9. Describe the purpose of a *pull request* in git. What is the goal of a *pull request*?
\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

10. Discuss the benefits of creating subsystems in different files. How does this practice help with the development 
      of a robot?
\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 


11. What is the point of the ```super()``` method in python?

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

12. What is the purpose of the ```__init__``` method in a python class?

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

\ 

13. Find the three errors in the following code:

```python
import wpilib from TalonFX, Solenoid


class Intake:
   
   def __init__(self):
      self.motor=TalonFX(motor_id)
      self.solenoid=Solenoid(1)

      
   def deploy(self, solenoid):
       self.solenoid.set(True)
       
   def retract(self, solenoid):
       solenoid.set(False)
       
   def run(self):
       self.motor.set_speed=1
       
   def stop(self):
       self.motor.stop()

```


