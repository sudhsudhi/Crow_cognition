import serial


port = "COM2"
ser = serial.Serial(port,9600)

value = 0

while True:
	value = ser.read()	
	print value