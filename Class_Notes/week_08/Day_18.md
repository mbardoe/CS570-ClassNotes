[comment]: render
# Day 18 CS570
## Control Theory Intro and SysId

## Introduction to Control Theory in FRC Robotics

### What is Control Theory?
Control theory is a fundamental concept in robotics and automation that allows us to regulate the behavior of a system. In the context of an FRC robot, control theory helps us manage motor speeds, arm positions, and other mechanisms to achieve precise movement. It involves:
- **Open-Loop Control** – sending commands without feedback
- **Closed-Loop Control** – adjusting commands based on sensor feedback
- **Feedforward Control** – predicting the necessary input to achieve a desired state

### Open-Loop Control
Open-loop control systems execute commands without considering sensor feedback. These systems are simple and work well when:
- The system operates in a predictable environment
- No external disturbances affect the output
- Precise control is not required

#### Example in FRC:
Setting a motor to a fixed speed:
```python
motor.set(0.5)  # Runs the motor at 50% power
```
The drawback is that variations in battery voltage, friction, or load changes can affect the actual speed of the motor.

### System Identification (SysID)
System Identification (SysID) is the process of determining the characteristics of a system so that we can better model and control it. In FRC, SysID is used to measure:
- **kS (Static Friction Compensation):** Minimum voltage required to overcome static friction
- **kV (Velocity Gain):** Relationship between voltage and steady-state velocity
- **kA (Acceleration Gain):** Relationship between voltage and acceleration

#### Running a SysID Test on a ROMI Robot
FRC provides tools in WPILib to generate a data-driven model for your system. Here’s how to set up and run a SysID test on a ROMI robot using RobotPy:

1. **Set Up SysID in WPILib**
   - Install the WPILib SysID tool using the WPILib tools installer.
   - Ensure your ROMI robot is properly configured and connected to your development computer.

2. **Deploy the SysID Logger**
   - Open the SysID tool and generate a project for ROMI.
   - Ensure you have `robotpy-wpilib`, `robotpy-wpimath`, and `robotpy-ctre` (if using CTRE motors) installed.
   - Deploy the SysID logger by placing the necessary script in your robot code and running `robot deploy` from your command line.

3. **Run the SysID Tests**
   - Select the type of test (quasistatic or dynamic) in the SysID interface.
   - Run forward and backward tests at low, medium, and high speeds.
   - The ROMI will execute controlled movements while logging data.

4. **Extract System Parameters**
   - After running the tests, collect the generated log files.
   - Upload the data into the WPILib SysID tool for analysis.
   - The tool will generate values for `kS`, `kV`, and `kA`.

5. **Use the Identified Values**
   - Implement the identified constants in your code:
   ```python
   from wpimath.controller import SimpleMotorFeedforward
   
   # Use values obtained from SysID analysis
   feedforward = SimpleMotorFeedforward(kS=0.2, kV=1.5, kA=0.3)
   voltage = feedforward.calculate(velocity=2.0, acceleration=1.0)
   motor.setVoltage(voltage)
   ```
   - This feedforward model will now help the ROMI move accurately based on the identified system characteristics.

### Implementing SysID on a ROMI Robot in Python
Below is a Python program that integrates SysID values and applies feedforward control to a ROMI robot:

```python
import wpilib
from wpimath.controller import SimpleMotorFeedforward
from wpimath.kinematics import DifferentialDriveKinematics

class RomiSysID(wpilib.TimedRobot):
    def robotInit(self):
        # Define motors
        self.left_motor = wpilib.PWMVictorSPX(0)
        self.right_motor = wpilib.PWMVictorSPX(1)

        # Invert one motor for proper drivetrain behavior
        self.right_motor.setInverted(True)

        # Create Feedforward Controller with SysID-identified parameters
        self.feedforward = SimpleMotorFeedforward(kS=0.2, kV=1.5, kA=0.3)

        # Kinematics for calculating wheel speeds
        self.kinematics = DifferentialDriveKinematics(trackWidth=0.14)  # Example ROMI width in meters

        # Initialize joystick for manual control testing
        self.joystick = wpilib.Joystick(0)

    def autonomousInit(self):
        # Set a target velocity (meters per second)
        self.target_velocity = 1.0  # Example velocity
        self.target_acceleration = 0.5  # Example acceleration

    def autonomousPeriodic(self):
        # Calculate required voltage using feedforward
        voltage = self.feedforward.calculate(self.target_velocity, self.target_acceleration)

        # Apply voltage to motors
        self.left_motor.setVoltage(voltage)
        self.right_motor.setVoltage(voltage)

    def teleopPeriodic(self):
        # Allow manual joystick override for testing
        speed = self.joystick.getY()
        rotation = self.joystick.getX()

        # Apply joystick inputs
        left_output, right_output = self.kinematics.toWheelSpeeds(speed, rotation)
        self.left_motor.set(left_output)
        self.right_motor.set(right_output)

if __name__ == "__main__":
    wpilib.run(RomiSysID)
```

### Feedforward Control
Feedforward control predicts the required input to achieve a desired state. This is especially useful when combined with closed-loop feedback for better accuracy.

The equation for feedforward control in a drivetrain:

\[ V = kS + kV \cdot velocity + kA \cdot acceleration \]

Where:
- **V** is the voltage sent to the motor
- **kS** compensates for static friction
- **kV** scales with velocity
- **kA** scales with acceleration

#### Implementing Feedforward Control in Python
Using WPILib’s `SimpleMotorFeedforward`:
```python
from wpimath.controller import SimpleMotorFeedforward

feedforward = SimpleMotorFeedforward(kS=0.2, kV=1.5, kA=0.3)
voltage = feedforward.calculate(velocity=2.0, acceleration=1.0)
motor.setVoltage(voltage)
```
This ensures that the motor receives an appropriate voltage to achieve the desired motion.

### Summary
- **Open-loop control** is simple but lacks precision.
- **SysID** helps identify motor characteristics for better control.
- **Feedforward control** predicts required inputs for smooth and accurate movement.

Understanding and implementing these concepts will improve your FRC robot’s performance, making it more responsive and reliable in competition.

