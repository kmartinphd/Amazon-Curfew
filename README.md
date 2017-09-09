# Amazon-Curfew
#### Objective
The  new, practical skill called Curfew is the latest addition to everyone's favorite Amazon Alexa. Directed for multiple people living in the same house, Curfew allows the user to ask Alexa everything they need to know about who is home. When you ask Alexa for who is home, Alexa responds with the names of who is home through finding their bluetooth devices. Curfew also allows the user to find out what time someone left or what time they arrived -- perfect for making sure your kids come home back in time for bed.
#### Mechanics
Curfew requires a Raspberry Pi 3 and the names and MAC addresses of their bluetooth phones must be connected and registered. The HomeApp runs the main program, the Sensor deals with the sensor information in its own thread, and InformationStorage saves any information of who is home and any goings in log files.
