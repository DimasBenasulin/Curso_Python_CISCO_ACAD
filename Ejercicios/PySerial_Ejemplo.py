import serial
ser = serial.Serial('COM7', 38400, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)  # open serial port
print(ser.name)         # check which port was really used
#ser.write(b'hello')     # write a string
ser.close()             # close port
