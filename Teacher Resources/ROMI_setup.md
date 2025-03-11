# ROMI Setup

## What is a ROMI?

ROMI is a small robot that can be programmed using ```wpilib``` and Python. 
It is a great way to learn about robotics and programming.

### Before the students get the ROMI's

#### Where do I get a ROMI

Romis can be purchased from [Pololu](https://www.pololu.com/category/203/romi-chassis-kits).

You need a raspberry pi as well, and a Micro SD card.


#### Setting up the ROMI

You will need to install a version of robotpy on the raspberry pi. This is similar for the
way that you would install robotpy on the RoboRio. The instructions to do this can be found 
at  [WPILibPI site](https://github.com/wpilibsuite/WPILibPi/releases). As of 3/25/2024 the 
WPILipPi version for 2024 does not support the ROMI. It is only for image processing.



You can connect to the ROMI via wifi at  http://10.0.0.2/ or http://wpilibpi.local/ to 
open the web dashboard. Note the image boots up read-only by default, so it's necessary 
to click the "writable" button to make changes. Connect to the WiFi SSID "WPILibPi-########" 
(the number is unique based on the Pi's internal serial number), WPA2 passphrase "WPILib2021!". 

There is information on the wpilib site about how to set up the ROMI.

[Setting up the ROMI](https://docs.wpilib.org/en/stable/docs/romi-robot/index.html)

### How Students use the ROMI

Students need to work in groups with the ROMI's because we only have about 7 right now.
The learning outcomes that I hope to achieve with the ROMI's include:

* Understanding of the basic structure of a robot code
* Opportunities to see how sensor data can be included in the programs
* Practice with PID tuning
* Practice with autonomous routines

### Basic ROMI Code

This is taken from the robotpy ROMI example:

```{python}
import os

import wpilib
from wpilib import TimedRobot, Joystick, Spark
from wpilib.drive import DifferentialDrive



class Tony_The_Robot(TimedRobot):

    def robotInit(self):
        '''This method is called as the robot turns on and is often used to setup the joysticks and other presets.'''
        self.controller=Joystick(0)
        self.left_motor=Spark(0)
        self.right_motor=Spark(1)
        self.drivetrain=DifferentialDrive(self.left_motor, self.right_motor)


    def robotPeriodic(self):
        '''This is called every cycle of the code. In general the code is loop
                 through every .02 seconds.'''

        pass

    def autonomousInit(self):
        '''This is called once when the robot enters autonomous mode.'''


        pass

    def autonomousPeriodic(self):
        '''This is called every cycle while the robot is in autonomous.'''
        pass

    def teleopInit(self):
        '''This is called once at the start of Teleop.'''
        pass

    def teleopPeriodic(self):
        '''This is called once every cycle during Teleop'''
        forward=self.controller.getRawAxis(0)
        rotate=self.controller.getRawAxis(1)
        self.drivetrain.arcadeDrive(forward, rotate)


if __name__ == "__main__":
# If your ROMI isn't at the default address, set that here
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wpilib.run(Tony_The_Robot)

```



