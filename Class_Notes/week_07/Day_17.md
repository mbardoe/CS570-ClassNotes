[comment]: render
# Day 17 CS570
## Quiz on Protocols, Gyros, PIDControllers, and RobotContainers

Name: ______________________________________

HC: ________________________________________


1. (10 pts) Write code for a Protocol called ```Motor``` theis protocol should have one method called ```set_raw_output```. 

<div style="page-break-after: always;">
\pagebreak 
</div>



2. (10 pts) Write a ```run``` method for an autonomous routine that asks a robot to move forward 2 meters. Use a PID 
controller to make sure that the robot moves forward the proper distance. You can assume that the PIDController
and other necessary objects were made in the ```init``` method.


<div style="page-break-after: always;">
\pagebreak 
</div>


3. (10 pts.) Fill in the blanks to make this **RobotContainer** work:

```python
import wpilib

from autoroutine import AutoRoutine
from drivestraight import DriveStraight
from drivetrain import Drivetrain
from gyroturn import GyroTurn


class RobotContainer:

    def __init__(self) -> None:
        self.controller = wpilib.Joystick(0)
        # Create SmartDashboard chooser for autonomous routines
        self.chooser = wpilib.______________________()
        self.drivetrain = Drivetrain()
        self._configure()

    def _configure(self):
        self.chooser.___________________("Twist 90 degrees", GyroTurn(self.drivetrain, 90))
        self.chooser.__________________("Go straight 2m", DriveStraight(self.drivetrain, 2))
        wpilib.SmartDashboard.________________(self.chooser)

    def get_autonomous(self) -> AutoRoutine:
        return self.chooser.____________()

```