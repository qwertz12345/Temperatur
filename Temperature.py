import serial
import sys
import time
#test
#test1
#test2
#test3
#ghfzug
ser = serial.Serial()
ser.baudrate = 9600
ser.port = "/dev/ttyACM0" #linux

def setupSerial():
	while True:
		try:
			ser.open()
			break
		except:
			print("could not open, trying again")
			time.sleep(1)
			try:
				ser.close()
			except:
				pass

# def setupFile(name):
# 	try:
# 		f = open(name, 'w')
# 		return f
# 	except:
# 		print("Could not open txt file")
# 		ser.close()
# 		sys.exit()

def callArduino():
	ser.flushInput()
	if ser.read(1)!='A':
		print("Arduino not ready, exiting...")
		ser.close()
		sys.exit()
	else:
		print("calling...")
		ser.write("calling")
		ser.flushInput()
		if ser.read(1)=='A':
			print("Arduino did not respond, exiting...")
			#sys.exit()
		else:
			print("Call succesfull.")

def closeAll():
	ser.close()
	f.close()
####################################################################################

setupSerial()
#setupFile("data.txt")
callArduino()
f = open("data.txt",'w')
for i in range(11):
	ser.flushInput()
	print(str(ser.read(4)))
closeAll()
# ser.close()
# f.close()
# print("Done.")