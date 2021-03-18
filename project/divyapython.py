import serial    //serial is a package 
                 // helps raspberry pi to connect to ardunio
                 // if we turn on/off the toggle switch in adafruit.io website, 
                 //its server will send the data to arduino uno board through raspberry pi3 model b serially
                 // serially means the data is sent byte by byte

from Adafruit_IO 
import Client, Feed, RequestError   //Adafruit_IO is a package and Client, Feed, RequestError are subpackages of it.

ser = serial.Serial("/dev/ttyACM0",9600,timeout=3)
//serial-->package name
//Serial("address of the port",BAUD rate,timeout=any seconds)-->function name
//"/dev/ttyACM0"-->address of the port of arduino in raspberian os
//BAUD rate-->how fast the communication is done
//timeout=3-->if arduino is not connected then it will try to connect for 3 seconds otherwise it will exit


ADAFRUIT_IO_KEY="*** type your key ***"

ADAFRUIT_IO_USERNAME="*** type your username ***"

aio=Client("*** type your username ***","*** type your key ***")// to raspberry pi the client is toggle button created in the website

digital=aio.feeds("***type your name of the button***")
//client has feed, recieve functions

while True:// it is infinite loop
	
    data=aio.receive(digital.key) // it returns dictionary

    print (data)

    if(data.value == "ON"):

       ser.write(b'1') //b-->byte // used to display on serial monitor on arduino ide

    elif(data.value == "OFF"):
	
       ser.write(b'0')

