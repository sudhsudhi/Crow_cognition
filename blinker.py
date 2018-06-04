import serial
ser=serial.Serial('COM7',9600)
ser.write('H')
while True:
    k=raw_input('H for on, L for off, Q to quit:')
    if k=='H':
        ser.write('H')
    elif k=='Q':
        break
    else:
        ser.write('L')


ser.write('L')
