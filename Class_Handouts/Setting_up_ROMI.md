# Romi instructions

### Setup up the Physical ROMI

The raspberryPi SD card will need the ROMI software put on to it. ROMI doesn't work with the 2023 version of robotpy so we are using the 2022 ROMI software.

Excellent instructions can be found ![here](https://docs.wpilib.org/en/stable/docs/romi-robot/imaging-romi.html)

The ROMI Image can be found ![here](https://github.com/wpilibsuite/WPILibPi/releases/tag/v2022.1.1)

Connecting to the ROMI wifi has password ```WPILib2021!```.

Then you can connect to the ROMI by accessing ```http://10.0.0.2/```

Once you have the correct version of python installed. (It may need to be the intel64 version.)

Then you can simply load the correct libraries into your pycharm project. Go to the terminal window of your python project. 

Then use the following commands:



```
pip install robotpy==2022.4.8
pip install robotpy'[commands2,sim]'
pip install robotpy-romi  ???
```

To get your robot to run you must type:

```
python robot.py sim --ws-client
```

### First Robot Program

Create a new PyCharm Project. Called First-ROMI. In this project create a file in the top directory called ```robot.py```. 

Then open a terminal window on the bottom of the screen and upload the necessary libraries:

```
pip3 install robotpy==2022.4.8
pip3 install robotpy'[commands2,sim]'
pip3 install robotpy-romi  
```

Now you can start to write your code. At the top of the ```robot.py``` make the necessary imports:

```python
import os
import wpilib
```

At the bottom of the document write the following code that will start our robot:

```python
if __name__ == "__main__":
    # If your ROMI isn't at the default address, set that here
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(MyRobot)
```

Now we will create the robot that we want to run. We do this by subclassing a particular kind of robot that is described in 
wpilib. 

```python
class MyRobot(wpilib.TimedRobot):    
    """
    Our default robot class, pass it to wpilib.run

    """

    def robotInit(self):
        pass
    
    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass
    
    def teleopInit(self):
        pass


    def teleopPeriodic(self):
        pass
```

This is the general structure of robots. 