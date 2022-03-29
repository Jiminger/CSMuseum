import time

import serial

ser = serial.Serial('/dev/tty.usbmodem14101', 115200, timeout=1)
ser.reset_input_buffer()

while True:
    numbers = input('Enter numbers: ')
    to_send = ('<' + numbers + '>')
    ser.write(bytes(to_send.encode()))
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    time.sleep(1)