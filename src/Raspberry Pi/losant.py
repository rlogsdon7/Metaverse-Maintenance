import json
import notecard
import notecard_pseudo_sensor
from periphery import I2C
import time
import obd
from obd import OBDStatus
import random
from tkinter import *
from PIL import ImageTk, Image

time.sleep(15)
connection = obd.OBD()
productUID = "com.ite.rlogsdon:metaverse_maintenance"
port = I2C("/dev/i2c-1")
card = notecard.OpenI2C(port, 0, 0)
req = {"req":"hub.set"}
req["product"] = productUID
req["mode"] = "periodic"
rsp = card.Transaction(req)
req = {"req":"card.location.mode","mode":"continuous"}
rsp = card.Transaction(req)
req = {"req":"card.aux","mode":"track"}
rsp = card.Transaction(req)
req = {"req":"card.location.track","start":True,"file":"location.qo","heartbeat":True,"hours":24}
rsp = card.Transaction(req)
req = {"req":"hub.sync"}
rsp = card.Transaction(req)
#print(rsp)
engLoad ="/" 
rpm = "/"
speed = "/"
timing = "/"
throttle = "/"
run = "/"
mil = "/"
purge = "/"
barr = "/"
volt = "/"
absLoad = "/"
curr_count = 1

def updateAttributes():
    global curr_count
    print(curr_count)
    curr_count = curr_count + 1
    connection = obd.OBD()
    if connection.status() == OBDStatus.CAR_CONNECTED:
        cmd4  = connection.query(obd.commands[1][4])
        cmd12 = connection.query(obd.commands[1][12])
        cmd13 = connection.query(obd.commands[1][13])
        cmd14 = connection.query(obd.commands[1][14])
        cmd17 = connection.query(obd.commands[1][17])
        cmd31 = connection.query(obd.commands[1][31])
        cmd33 = connection.query(obd.commands[1][33])
        cmd46 = connection.query(obd.commands[1][46])
        cmd51 = connection.query(obd.commands[1][51])
        cmd66 = connection.query(obd.commands[1][66])
        cmd67 = connection.query(obd.commands[1][67])
        cmd68 = connection.query(obd.commands[1][68])
        engLoad = cmd4.value.magnitude
        rpm = cmd12.value.magnitude
        speed = cmd13.value.magnitude
        timing = cmd14.value.magnitude
        throttle = cmd17.value.magnitude
        run = cmd31.value.magnitude
        mil = cmd33.value.magnitude
        purge = cmd46.value.magnitude
        barr = cmd51.value.magnitude
        volt = cmd66.value.magnitude
        absLoad = cmd67.value.magnitude
    elif True:
        engLoad = random.randrange(0,100)
        rpm = random.randrange(0,7000)
        speed = random.randrange(0,100)
        timing = random.randrange(0,100)
        throttle = random.randrange(0,100)
        run = random.randrange(0,6000)
        mil = random.randrange(0,1)
        purge = random.randrange(0,100)
        barr = random.randrange(65,135)
        volt = random.randrange(8,15)
        absLoad = random.randrange(0,100)
    if (curr_count % 5 == 0):
        req = {"req":"note.add"}
        req["file"] = "new.qo"
        req["sync"] = True
        req["body"] = {"G":connection.status(),"E":engLoad,"RPM":rpm,"S":speed,"T":timing,"TP":throttle,"R":run,"M":mil,"EP":purge,"B":barr,"C":volt,"A":absLoad}
        rsp = card.Transaction(req)
        print(rsp)
    
    xspeed.config(text= "   " + str(speed) + "   ")
    xTP.config(text= "   " + str(throttle) + "   ")
    xRPM.config(text= "   " + str(rpm) + "   ")
    xENG.config(text= "   " + str(engLoad) + "   ")
    xTiming.config(text= "   " + str(timing) + "   ")
    xVoltage.config(text= "   " + str(volt) + "   ")
    xVoltage.after(3000,updateAttributes)

root=Tk()
root.geometry("1024x600")
img = ImageTk.PhotoImage(Image.open("Logo.png"))
#Row 0
logo = Label(root, image = img)
logo.grid(row=0,column=0,columnspan=300,pady=30)
#Row 1-3
speedLabel=Label(root,text="Speed",font="times 24 bold")
speedLabel.grid(row=1,column=1)
speedHolder=Label(root,text ="          ",font=("times",60,"bold"),bg="white")
speedHolder.grid(row=2,column=1,pady=10,padx=10,ipady=10)
xspeed=Label(root,font=("times",60,"bold"),bg="white")
xspeed.grid(row=2,column=1,pady=10,padx=50,ipady=10)
speedUnit=Label(root,text="MPH",font="times 15 bold")
speedUnit.grid(row=3,column=1)

RPMLabel=Label(root,text="Revolutions Per Minute",font="times 24 bold")
RPMLabel.grid(row=1,column=2)
RPMHolder=Label(root,text ="          ",font=("times",60,"bold"),bg="white")
RPMHolder.grid(row=2,column=2,pady=10,padx=50,ipady=10)
xRPM=Label(root,font=("times",60,"bold"),bg="white")
xRPM.grid(row=2,column=2,pady=10,padx=50,ipady=10)
RPMUnit=Label(root,text="RPM",font="times 15 bold")
RPMUnit.grid(row=3,column=2)

TPLabel=Label(root,text="Throttle Position",font="times 24 bold")
TPLabel.grid(row=1,column=3)
TPHolder=Label(root,text ="          ",font=("times",60,"bold"),bg="white")
TPHolder.grid(row=2,column=3,pady=10,padx=50,ipady=10)
xTP=Label(root,font=("times",60,"bold"),bg="white")
xTP.grid(row=2,column=3,pady=10,padx=50,ipady=10)
TPUnit=Label(root,text="%",font="times 15 bold")
TPUnit.grid(row=3,column=3)

#Row 4-6
BlankLabel=Label(root,text="   ",)
BlankLabel.grid(row=4,column=1,pady=20)
#Row 5-7
ENGLabel=Label(root,text="Engine Load",font="times 24 bold")
ENGLabel.grid(row=5,column=1)
ENGHolder=Label(root,text ="          ",font=("times",60,"bold"),bg="white")
ENGHolder.grid(row=6,column=1,pady=10,padx=10,ipady=10)
xENG=Label(root,font=("times",60,"bold"),bg="white")
xENG.grid(row=6,column=1,pady=10,padx=50,ipady=10)
ENGUnit=Label(root,text="%",font="times 15 bold")
ENGUnit.grid(row=7,column=1)

VoltageLabel=Label(root,text="Controle Module Voltage",font="times 24 bold")
VoltageLabel.grid(row=5,column=2)
VoltageHolder=Label(root,text ="          ",font=("times",60,"bold"),bg="white")
VoltageHolder.grid(row=6,column=2,pady=10,padx=50,ipady=10)
xVoltage=Label(root,font=("times",60,"bold"),bg="white")
xVoltage.grid(row=6,column=2,pady=10,padx=50,ipady=10)
VoltageUnit=Label(root,text="Volts",font="times 15 bold")
VoltageUnit.grid(row=7,column=2)

TimingLabel=Label(root,text="Timing Advance",font="times 24 bold")
TimingLabel.grid(row=5,column=3)
TimingHolder=Label(root,text ="          ",font=("times",60,"bold"),bg="white")
TimingHolder.grid(row=6,column=3,pady=10,padx=50,ipady=10)
xTiming=Label(root,font=("times",60,"bold"),bg="white")
xTiming.grid(row=6,column=3,pady=10,padx=50,ipady=10)
TimingUnit=Label(root,text="Degrees",font="times 15 bold")
TimingUnit.grid(row=7,column=3)


updateAttributes()
root.mainloop()

