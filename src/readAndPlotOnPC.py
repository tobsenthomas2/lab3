
# #for the controler we need to change a file and the send datat like this
#code classnotebook: https://cpslo-my.sharepoint.com/personal/crefvem_calpoly_edu/_layouts/15/Doc.aspx?sourcedoc={94383b5e-1602-443c-822b-e03c434c9049}&action=view&wd=target%28_Lecture%20Notes%2FSection%2001.one%7C55db1e55-014b-4a31-8024-ff1c5151a70a%2FCharacter%20I%5C%2FO%20Using%20pyb.USB_VCP%20%7Cc5a1326e-ba0c-42c2-ad94-b665f1864fb7%2F%29&wdorigin=NavigationUrl

#code instruction
# u2 = pyb.UART(2, baudrate=115200)      # Set up the second USB-serial port

# for number in range(10):               # Just some example output
#     u2.write(f"Count: {number}\r\n")   # The "\r\n" is end-of-line stuff
#     number += 1


# import serial
#    ...
#    with serial.Serial ('COMx', 115200) as s_port:
#        ...
#        s_port.write (b'something')       # Write bytes, not a string
#        ...


#reading:
#print (s_port.readline ().split (b','))


import sys
sys.path.append('c:/users/admin/anaconda3/lib/site-packages')
#issue: serial module not found --> pip show pyserial and add the path
import serial
import time
from matplotlib import pyplot

#cant start program from "usaual" python terminal --> use thonny python and use the following command
#& 'C:\Program Files (x86)\Thonny\python.exe' .\readAndPlotOnPC.py

def plot_data(input):
    x = []
    y = []
    for line in input:
        #print(line)
        #data = line.split(',')
        data=line
        try:
            x_val = float(data[0])
            y_val = float(data[1])
            x.append(x_val)
            y.append(y_val)
        except ValueError:
            # ignore row if data is not a float
            pass
    pyplot.plot(x, y)
    pyplot.title("best guess - Kp good")
    pyplot.xlabel("time")
    pyplot.ylabel("value")
    print("MAX Value: "+ str(max(y)))
    pyplot.show()

with (serial.Serial("COM5",115200) as ser):
    #ser.flush() #clear Input buffer
    #ser.in_waiting()#NUM of CHArs in Buffer

    #ser.read(n)
    #ser.readlines()#read until \n or \r
    #ser.readlines()
    morePlots=True
    while morePlots:
        ser.flushInput()
        ser.flushOutput()
        data=[]
        dataStream=1
        while dataStream:
            buf=ser.readline ().split (b',')

            data.append(buf)
            if buf==[b'99999', b'99999\r\n']:
                dataStream=False
                print("end works!")
                data.pop()
                if(ser.readline ().split (b',')==[b'99999', b'99999\r\n']):
                    print("last plot. you can stop now")
                    morePlots=False
            print(buf)

        plot_data(data)
        
    time.sleep(5)
    print("last dataset was sent! will stop listening now")
    


