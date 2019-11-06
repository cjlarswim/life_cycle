#Flashing XAVIER Via VM

##Purpose
This document is to describe the process of flashing the Jetson Xavier AGX Developer Kit (P2888) running Ubuntu 18.04 in a 
virtual machine on MacOS Catalina (10.15). 
Flashing the Xavier via a virtual machine (VM) is not officially supported. 
While there is clear [a link](https://www.developer.nvidia.com/nvidia-sdk-manager) documentation and a great video by Jim 
from JetsonHacks.com [a link](https://www.jetsonhacks.com/2019/06/04/nvidia-sdk-manager-for-jetson-jetpack-4-2/)on how to 
flash the Xavier via a Ubuntu Host Computer there is only some unresolved threads in the Nvidia Developer Forum on how to flash via VM.

The Process does require some tinkering around and is not guranteed to work. Following the steps and setup we used to get the Xavier up and running.

##Hardware Setup
For a reference of the necessary hardware Setup see the great Video of Jim from JetsonHacks.com:
[a link](https://www.youtube.com/watch?v=Pncjv6FoQzU&t=155s)

For our Setup via Mac we needed following hardware:

- gigabit ethernet switch or router connected to the internet
- two Cat5 ethernet cables
- one USB-C to ethernet adapter
- three USB-C to USB adapters

##VirtualBox 6.0
VirtualBox 6.0 enables you to run any operating System parallel to your hosts machine OS. 
While running it will use resources (which will be predetermined during setup) from your host machine.
The process of setting up the Virtual Machine is documented well.
Please refer to the manual for initial setup.

[a link] (https://download.virtualbox.org/virtualbox/6.0.14/UserManual.pdf)

We allocated following resources to our VM running Ubuntu 18.04.

**12GB of Memory**

**100GB of HDD Space**
    
In this case we used an exertnal HDD to allocate that much HD space. See page 9&10 of VB User Manual.
    During Setup:
    ![Create Virtual Machine HDD](https://user-images.githubusercontent.com/25865287/68291165-96475c00-0089-11ea-88b5-8bcbcbed3f7d.jpeg)
      *create a virtual HDD now*
    ![Select File Location & Size](https://user-images.githubusercontent.com/25865287/68291202-a5c6a500-0089-11ea-9fc7-08be614d509e.jpeg)
      *chose your external HDD and alocate 100GB of space*

Now your virtual machine is set and ready.
Start Ubuntu 18.04 via Virtual Box and Download the SDKManager from Nvidias WebPage.

##Steps to Flash
###Install Python 3.7 on Guest Machine
In Terminal run:
`sudo get apt-install Python`

after installation check for Python version in Terminal:
`python3`

>We are not sure why python3 has to be installed. However, after some reasearch in the Nvidia Developer Forums we decided to do so. Anyway, Python never hurts. The installation process did run smoothly after doing so. :relaxed:

###Download and run SDKManager [a link](https://www.developer.nvidia.com/nvidia-sdk-manager)
After Download from the website. Run in Terminal:
`sudo apt install ./(*insert* your sdkmanager file)`

Run SDKManager via Terminal:
`sdkmanager`

Login and follow the instructions.
*Tip:* **Hit the checkbox 'Autologin'**


##Install | Build OS (Ubuntu & Jetson) | Flash

>In order for the Jetson to be flashed in needs to be directly connected to your guest machine. However, the USB-C ports of 
>your Mac are used by the host machine and generally not recognized by the guest. Follow these steps to make your Xavier 
>visible on the guest machine.

>This process has to be repeated when the SDKManager is not able to flash the Xavier due to lack of a connection via USB.
>The flashing process is separated in different stages during the process via SDKManager.

>Whenever, the SDKManager throws the error - no connection to Board via USB - while trying to flash
>**skip this step**
>**finish the install**
>**power off the virtual machine**
>**run Xavier in recovery mode or on OS** 
>**add the board to your USB Filters in Virtual Box.**
>**Restart VM**
>**restart SDKManager**
>**follow the steps of the installation manager**

>Once the board is up and running on the 18.04 Ubuntu OS there is no need to put it back into recovery mode the board >should be recognized by VB immediately.

The SDKManager will download all necessary files, build and install the OS. At some point it will ask you to flash the Xavier board.

*Hit Skip.*

*Finish the Install.*

*Power Off the virtual machine.*

*boot your Nvidia Xavier into recovery mode* 
[a link](https://developer.ridgerun.com/wiki/index.php?title=Xavier/Flashing_the_Board)
`1. Power down the device. If connected, remove the AC adapter from the device. The device must be powered OFF, and not in a suspend or sleep state.
2. Connect the Type-C plug on the USB cable to the Recovery (USB Type-C) Port on the device and the other end to an available USB port on the host PC.
3. Connect the power adapter to the device.
4. Press and release the POWER button to power on device.
5. Press and hold the FORCE RECOVERY button: while pressing the FORCE RECOVERY button, press and release the RESET button; wait two seconds and release the FORCE RECOVERY button.
6. When the device is in recovery mode, lsusb command on host will list a line of "NVidia Corp"
In VB hit Settings.`

*Allocate USB-C port to guest machine*

Navigate to **Ports** --> **USB**

Enable **USB Controller** --> Enable **USB 3.0 (xHCI) Controller**

Use the toggles on the right hand side to add a new USB Filter. The Xavier should show up as Nvidia Corp. *Enable*
![add USB port to Guest](https://user-images.githubusercontent.com/25865287/68293801-01476180-008f-11ea-888f-39bb0ef5a0ed.jpeg)

*Power your VM back on*

*Run SDKManager via Terminal*

*Follow instructions provided*
