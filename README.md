# _life_cycle()_
## A machine vision enabled, intelligent traffic signal, warning right turning drivers from incoming cyclist. 

The essential idea of _Life_Cycle()_ is to reduce traffic accidents involving cars and bicycles in unclear turning situations. Hence, reducing the number of hurt or killed bicyclists in the city. _Life_Cycle()_ is a camera based, machine vision enabled system running the [_Darknet YOLO Framework_](https://pjreddie.com/darknet/yolo/), which can identify incoming cyclist, while approaching an intersection and warn turning vehicles only if an accident is about to occur. The prototyp is based on the [OpenDataCam by Moovel](https://www.move-lab.com/project/opendatacam/) and has been created in direct collaboration with the great staff of their Berlin office.
The system is ought to be implemented where traditional systems, such as mirrors or protected bike lanes fail to work. 

This system is especially valuable for following situations 
- _the bike lane cannot be observed directly by the car driver :truck:_
- _at temporary construction sites :construction:_
- _in situations where the bike path is not observable by turning assistants :point_right:_

While turning assistants are a valid option for some traffic participants (i.e truck drivers), only 5% of all trucks on German roads are equipped with such a system. It will take another 20 years or so for the car and truck population to adapt a great enough turning assistant density to have a significant effect on safety on city roads for cyclist.
Our system can be implemented quickly and at relatively low cost, hence, creating a higher level of safety at crossings which have been identified as dangerous.

![The Way it is supposed to work](https://user-images.githubusercontent.com/25865287/69149813-9870d800-0ad7-11ea-9e34-ff48cc96e01a.jpeg)

## Setup Your Own Prototyp
Due to a memory leak caused by OpenCV we still decided to use the raspberry pi to fetch the data, process, and trigger. We are currently working on running all processing on the Jetson Board. 
We also included a type of error handling: before the Jetson board crashes we restart via a sudo command from the Raspberry.

### Hardware & Setup
To build your own Life_Cycle() Prototype to test and develope new ideas and use cases you will need following hardware:

#### Hardware Installation
For installation of UBUNTU 18.04 onto _Jetson Boards_ and _Raspberry PI_ out of the box you will need:
- a USB Mouse
- a USB Keyboard
- a monitor with an HDMI connector

[For general Setup of Jetson Xavier Go Here](https://www.jetsonhacks.com/2018/10/05/jetpack-4-1-developer-preview-nvidia-jetson-agx-xavier-developer-kit/)

[For Setup Jetson Xavier via a VM follow our guide](https://github.com/cjlarswim/life_cycle/blob/master/documentation/XavierSetupViaVirtualMachine.md)

[For Raspberry Pi Setup Go Here](https://www.raspberrypi.org/documentation/)


#### Processing and Object Detection
- [Nvidia Jetson Nano or TX2 or or Xavier](https://developer.nvidia.com/embedded/develop/hardware)
- USB Cam or CSI Cam
  - Most USB Cams will be supported by the Jetson Boards
  - For Setup we used the [Raspberry Cam](https://www.amazon.de/Electreeks-Raspberry-Kamera-Modul-Infrarot/dp/B0763Q5ZBS/ref=sr_1_2?__mk_de_DE=ÅMÅŽÕÑ&keywords=imx219&qid=1574165237&sr=8-2) Module with an IMX219 chip
    - for Setup of a CSI connected cam use following [Instruction](https://github.com/opendatacam/opendatacam/blob/master/documentation/jetson/JETSON_NANO.md#experimental-use-raspberry-pi-cam-with-opendatacam-default-installation) while these instructions have been flagged as experimental - our setup worked just fine with it.

#### Processing and Trigger
- Raspberry 3, 3B, 3B+ or 4 (you will probably get away with older models as well, but we have not tested them yet)
- Relais Module
- lamp running on 230V (or any other type of trigger will do)

![Setup Scheme](https://user-images.githubusercontent.com/25865287/69146282-c3572e00-0acf-11ea-82cc-136b21c07b76.jpeg)

### Connect & Test
#### Network
You can establish a network by setting up your raspberry as a hotspot. However, we experienced very low bandwith and hence low performance while testing. This will show as time lags in the detection and triggering of your warning signal. 

Alternatively you can create a setup connecting both machines via an ethernet box. 
_insert Image of Network Setup here with explanation_

_insert Image of Setup_

#### Connect (see image above)
#### check for connection via router
#### assign steady IP adresse
#### connect via SSH

### Implement Python Code
Safe this [code](scripts/raspyprocessing.py) on your Raspberry Pi

use _touch_ to create file
```
touch file_name.py
```

use _nano_ to edit file
```
nano file_name.py
```

To start the code on startup of your Raspberry put the scriptpath in here 
```
sudo nano /etc/rc.local
```
