# Fresnel_Ultrasound_Project
This repository contains the code used in a project to automate an experiment on Fresnel diffraction
Picoscope
Using SDK and wrapper from https://github.com/colinoflynn/pico-python.git.
Code, after imports, opens scope collects data with get block 
Voltage and time data, plots
Iterate get block for averaging the data
Simple trigger - trigger on square wave, rising or falling edge
Set times base - waveform 


# Stepper Motor
20cm in 50 rotations
Limit switches installed

Micropython on pico 

U2if firmware installed on pico
Packages from ADAFruit website https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-raspberry-pi-pico/setup
Note: not u2if directly from source - installs different HIDAPI libraries that are incompatible
Circuit python and Blinka
Blinka, digital in/out commands, send True/False (high and low) to GP pins 2,3.
Pin 2 is step, pin 3 direction. (GP2, GP3) - Step, Dir pins on driver

# Big Easy Driver from Schmalz Haus: 
http://www.schmalzhaus.com/BigEasyDriver
DIR: When high, the motor will turn counterclockwise, and when low, the motor will turn clockwise
STEP: Each rising edge of this input will cause the stepper driver to advance one step in the direction specified by the DIR input. The STEP input must be high for at least 1us, and low for at least 1us

# Pyserial
Using pyserial to communicate to pico, run main.py on pico and send function commands
http://blog.rareschool.com/2021/01/controlling-raspberry-pi-pico-using.html

Saved stepping code on raspberry pi using Thonny as main.py

Run pip install pyserial.

example of running:
Copy sender.py from http://blog.rareschool.com/2021/01/controlling-raspberry-pi-pico-using.html into an editor and save it in a directory of your choice.
In that directory, run python3 to start an interactive session.
Type from sender import Sender
Type s = Sender(). If you are running on Windows, you will need to type s = Sender('COM6') replacing COM6 by whatever port the Pico is visible on.
Type s.send('2 + 2')
Type s.receive(). If all is well, this will print the result 4.
When you have finished, type s.close().

sender class defined at beginning of Python notebook in this case
