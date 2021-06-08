# Code-of-Pi
This file holder is contain the code of water pump, 2-DOF platform, soil sensor driver.<br>
The codes of writen by python in Raspberry Pi 4b
 
"main.py" is the main function to  control each part, when the socket push message to Pi.<br>
It would be decoded to "[x,x,x,x]" matrix, when the weed come into the camera field of view<br>
the computer will accurately identify them and mark the location information of weeds. 
After calculation and conversion, the target Angle information will be fed back to the cradle head for aiming.


# Using D435i camera in Paspberry Pi 4b(Deprecated)
[install](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation_raspbian.md)
