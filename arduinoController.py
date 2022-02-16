import serial


if __name__ == '__main__':

    ser = serial.Serial('/dev/tty.usbmodem14101', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:

        user = input("Enter input: ")
        if user == '1':
            x = '0'
            y = '60'
            ser.write(bytes(x, 'utf-8'))
            ser.write(bytes(y, 'utf-8'))
        elif user == '2':
            x = '5'
            y = '10'
            ser.write(bytes(x, 'utf-8'))
            ser.write(bytes(y, 'utf-8'))
        elif user == '0':
            x = '0'
            y = '20'
            ser.write(bytes(x, 'utf-8'))
            ser.write(bytes(y, 'utf-8'))
