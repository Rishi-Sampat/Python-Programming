import serial
import time

arduino=serial.Serial(port='COM9',baudrate=115200,timeout=1)
time.sleep(2)

message=input("Enter message to send to Arduino: ")
arduino.write((message + "\n").encode())

print("Message sent to Arduino!")