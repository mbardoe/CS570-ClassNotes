[comment]: render
# Day 9 CS570
## Test on Git/GitHub/OOP/TimedRobot

**Name:** __________________________________________________________


**HC:** ________________________________________________________________


1. (6 points) Your robot is working well, but it doesn't have a climber. The code is checked and working, and is all consolidated
on the ```main``` branch of the git repository. How would you use git to add new code to your repository? 

\

\

\

\

2. (14 points) Write a class ```Climber``` class in python with following requirements (you don't have to worry about imports):

    * The Climber class ```__init__``` takes in two arguments (beyond the required ```self```: the first is the cancoder 
      id of the motor that runs the climbing 
      action. The second is an id number for the pneumatic actuator (solenoid) that releases the climber.
    * Instantiate a ```Motor``` class using as an input the cancoder id that was given in the initialization.
    * Instantiate  a ```Solenoid``` using as an input the id that was given in the initialization. Then make sure the Solenoid
      is engaged by using the ```set``` method of the Solenoid and passing in the value ```True```.
    * The class has a ```release``` method that releases the climber, which uses the ```set``` method of the ```Solenoid```
        and passes in the value ```False```.
    * The class has a ```climb``` method that uses the ```Motor```'s ```run``` method passing in the value 1.
    
<div style="page-break-after: always;">
\pagebreak 
</div>


3. (6 points) Your teammate Dick has been working on some code to add to our competition robot. This code
is going to help run the robot's intake. He feels that he is done, so he merged his changes into the main branch.
Did Dick do the right thing? Why or why not? If he did not do the right thing, what should he have done?

<div style="page-break-after: always;">
\pagebreak 
</div>


5. (12 points) Fill in the blanks.



6. (6 points) 

Kendra is considering making a change to the base code that has run the intake for the last several seasons, 
because they want to add some further functionality to the intake. How could Kendra use sublclassing to make 
the job of writing new intake code easier. 


\

\

\

\

7. (9 points) Bob has written the code below. Please identify at least 3 mistakes in the code:

```python
import wpilib from Spark, Solenoid


class Intake:
   
   def __init___(self):
      self.motor=Spark(motor_id)
      self.solenoid=Solenoid(1)

      
    def deploy(self, solenoid):
       self.solenoid.set(True)
       
    def retract(self, solenoid):
       solenoid.set(False)
       
    def run(self):
       self.motor.set_speed=1
       
       

```

\

8. (6 points) You have a teammate, Muma, that wants to write all the code to run the robot in one file. 
What are some reasons that this is a suboptimal idea? 



