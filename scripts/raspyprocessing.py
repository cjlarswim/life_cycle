import time
import requests
import json
import RPi.GPIO as GPIO
import paramiko
import webbrowser


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW);
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW);

#1 open shell and START docker container with ODC

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

#2 open Browser to initiate ODC

def startBrowser():
    webbrowser.open("192.168.0.102:8080")

#3 draw line and start recording <- manual or automatically?

#4 Check for current recording

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

#5 check if current recording is still on
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

#7 TODO:open shell and STOP docker container 


#------------------------------------------------------------------------------------------------------

#Connect to Jetson and Start Container
startSSH()

#Check for Person Move
CheckForMove()






