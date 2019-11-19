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

>insert Live Use Case Video

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
#### Network
You can establish a network by setting up your raspberry as a hotspot. However, we experienced very low bandwith and hence low performance while testing. This will show as time lags in the detection and triggering of your warning signal. 

Alternatively you can create a setup connecting both machines via an ethernet box. 
_insert Image of Network Setup here with explanation_

### Connect & Test
_insert Image of Setup_

#### Connect (see image above)
#### check for connection via router
#### assign steady IP adresse
#### connect via SSH

### Implement Python Code

1. Import packages
```
  import time
  import requests
  import json
  import RPi.GPIO as GPIO
  import paramiko
  import webbrowser
```

2. Set initial GPIO value and specify output pin
```
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW);
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW);
```

3. open shell and START docker container with ODC

```
def send_string_and_wait(command, wait_time, should_print, shell):
    # Send the su command
    shell.send(command)
    # Wait a bit, if necessary
    time.sleep(wait_time)
    # Flush the receive buffer
    receive_buffer = shell.recv(1024)
    # Print the receive buffer, if necessary
    if should_print:
        print receive_buffer

def startSSH():
    # Create an SSH client
    client = paramiko.SSHClient()
    # Make sure that we add the remote server's SSH key automatically
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the client
    worker = 0
    while worker == 0:
        try:
            client.connect('192.168.0.102', username='life_cycle', password='lifecycle')
            worker = 1
        except:
            print("No Connection to @lifecycle")
            time.sleep(10)

    #Create a raw shell
    shell = client.invoke_shell()
    # Send the su command
    send_string_and_wait("sudo docker start 84f49b59336c\n", 3, True, shell)
    system_su_password ="lifecycle"
    #Send the client's su password followed by a newline
    send_string_and_wait(system_su_password + "\n", 3, True, shell)
```
4. Open Browser to initiate ODC
```
def startBrowser():
    webbrowser.open("192.168.0.102:8080")
```
5. draw line and start recording <- manual or automatically?
```
_insert_
```
6. Check for current recording
```
def getStatus():
    currentRecording = None
    while currentRecording is None:
        try:
            status= "http://192.168.0.102:8080/status"
            getStatus = requests.get(status)
            statusData = getStatus.json()    
            print("Getting current Recording")
            currentRecording = statusData["appState"]["recordingStatus"]["recordingId"]
            print("Current Recording ID: {}".format(currentRecording))
        except:
            pass
    return (currentRecording)
```
7. check if current recording is still on
```
def CheckForMove():
    CountPerson = 0
    while True
        try:
            #Check Current Recording ID    
            currentRecording = getStatus()
            activeCounter = 'http://192.168.0.102:8080/recording/{}/counter'.format(currentRecording)
            r = requests.get(activeCounter)
            data = r.json()
            print("Check for detection")
            #If no Person has been detected, the Json File wil not have the person entry. This will throw an Error
            # which will be caught and pass. Since while is true loop will start again.
            CountPersonNew = data["counterSummary"][list(data["counterSummary"].keys())[0]]["person"]

            if CountPersonNew > CountPerson:
                print("Person Detected")
                lightswitch()
                CountPerson = CountPersonNew
            time.sleep(1)
        except:
            pass

def lightswitch():
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    time.sleep(1)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    time.sleep(1)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    time.sleep(1)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
```
```
8. TODO:open shell and STOP docker container 


#------------------------------------------------------------------------------------------------------

#Connect to Jetson and Start Container
startSSH()

#Check for Person Move
CheckForMove()
```

### Run

## Other Use Cases
The systems main application is to warn drivers during the turning process. However, other applications can be realized using the exact same setup, possibly running parallel to the exisiting live application (depending on the physical setup and the range of view the camera can identify certain elements with confidence).

### Use as monitoring device for passing cars @strategically sound points in the city (z.B Umweltplakete)
Currently there is no way for cities to monitor incoming traffic based on EURO 1-6 emissions standards for cars. Possibly, the camera can be trained to visually identify the EURO-Plakette indicating the emission standard of the incoming cars.  

Get your Nerd on and check how it is done in Berlin measuring air quality and calculating statisticaly values [here in German!](https://www.berlin.de/senuvk/umwelt/luftqualitaet/umweltzone/download/umweltzone_1jahr_bericht.pdf)

### Speed Monitoring 
It does not make sense to put speedometers everywhere in the city. However, many policies (f.e [Berlin Air Purity Plan](https://www.berlin.de/hauptstadtluft/en/improving-air-quality/air-purity-plan/) depend on monitoring to ensure that the policies in place are effective. Traffic and traffic speed play an important role here. Once a policy is in place, f.e. tempolimit 30km/h, the policy is only as good as the monitoring and the steps taken to improve the policy. Today, there is no way to actually monitor streets efficiently at low cost. 
Life_Cycle could take that part to monitor speedsters and count the total amount at places where it is installed anyway to save cyclists' lifes. 
Policies can then be adapted moving from a soft (f.e tempolimit) approach to harder approaches (f.e police control, speedometer, speedbumps, etc) if needed.

### Accident forensics & Video Material to train neural networks
Collected video material can be used to deal with questions arising after an accident has happened. Also the video material can be used to train neural networks dealing with predicting accidents. 
Currently, the video is not saved after being processed. However, in order to create new insights the network can be trained to identify when an accident has happened and keep a predetermined range of video material on a disk connected to the setup which otherwise will be deleted every x minutes. 

### Life observation of several intersections
The prototype currently works with one camera monitoring a certain area. However, with the power of the new Jetson XAVIER up to 16 CSI Cameras can be attached to the camera to monitor many different areas of one intersection creating a dense Network of monitoring and warning signals at minimum cost.

### Counting passing traffic participants at crossing (quantitativ analysis)
The initial setup [OpenDataCam](https://www.move-lab.com/project/opendatacam/) by Moovel has been inveneted for counting traffic on different levels. Participants who are ususally left out (bikes, pedestrians, scooters, skaters, etc.) in quantitative observations can now be quantified. For certain areas this data can lead to new insights why certain areas fluctuate in traffic. For more insights and further projects visit their website and watch their video below :point_down:

<a href="https://vimeo.com/346340651"><img src="https://www.move-lab.com/project/opendatacam/static/images/about-2.jpg" alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
