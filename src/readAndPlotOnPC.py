import sys
sys.path.append('c:/users/admin/anaconda3/lib/site-packages')
#issue: serial module not found --> pip show pyserial and add the path
import serial
import time
from matplotlib import pyplot

#cant start program from "usaual" python terminal --> use thonny python and use the following command
#& 'C:\Program Files (x86)\Thonny\python.exe' .\readAndPlotOnPC.py

"""!
 * @brief Plots data received from the serial port.
 * @param[in] input the data to be plotted.
"""
def plot_data(input):
    x = []
    y = []
    plotNr=0
    for dataToPlot in input:
        dataBuf=dataToPlot

        for line in dataBuf:
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
        if  plotNr%4==0:
            pyplot.plot(x, y,color='g',label=str(plotNr))
        elif plotNr%4==1:
            pyplot.plot(x, y,color='b',label=str(plotNr))
        elif plotNr%4==2:
            pyplot.plot(x, y,color='r',label=str(plotNr))
        elif plotNr%4==3:
            pyplot.plot(x, y,color='y',label=str(plotNr))
        pyplot.legend(loc="upper left")
        pyplot.title("Plot")
        pyplot.xlabel("time [ms]")
        pyplot.ylabel("position [encoder ticks]")
        print("MAX Value: "+ str(max(y)))
        
        if plotNr%4==0 and plotNr!=0:
            pyplot.figure()
            
        print("plot nr: " + str(plotNr))
        plotNr+=1
    pyplot.ion()
    pyplot.show()
    pyplot.pause(0.1)
    
"""!
 Main function that reads and plots data from the serial port.
 """

with (serial.Serial("COM5",115200) as ser):

    morePlots=True
    plotCounter=0
    dataStorage=[]
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
                print("end this data set!")
                data.pop()
                if(ser.readline ().split (b',')==[b'99999', b'99999\r\n']):
                    print("last plot. you can stop now")
                    morePlots=False
            #print(buf)
        dataStorage.append(data)
        plot_data(dataStorage)
        dataStorage=[]
        
    
    print("last dataset was sent! will stop listening now")
    input("press enter to exit")  



