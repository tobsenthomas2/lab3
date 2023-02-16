# lab3
ME-405-03-2232 lab3

#Instruction
The goal of this lab was it to test diffent period times for our motor tasks. The timespan should be as long as possible without seeing a to big decrease in performance. For that we changed the period values manualy, then the controller should move the motor to a specific position. After teh posotion is arrived the STM32 send a data set of the position and time to the PC, where we plot the data and the Maxima to check the overshoot and for discontinuity. The beste perios we had was 60 ms. Here we had a 2,5% higher value compared to the original perios of 10ms. This seems good to us. You can see the datatset in the following plot:
![alt text](https://github.com/tobsenthomas2/lab3/blob/main/FigurePeriodsTill60.png)


We also tried different higher values to see when it is getting really bad. The discontunuity starts at 110 ms, before that only the overshoot is a problem. You can see that in the following Plot:

![alt text](https://github.com/tobsenthomas2/lab3/blob/main/PlotPeriodsTill200.png)


# How to use the programs:

To use this motor controller for two motors, run the main function and input the desired angle (in encoder ticks), and the desired Kp value. Depending on your motor this value may have to be adjusted. To plot the response, run the readAndPlotOnPC.py program, with your computer attached to the ST-LINK on the micro controller. Ensure that the port is set to the correct USB terminal on your computer. This is in addition to the cable you have set up to run micropython on the micro controller. Now run the main program and wait for the motion to stop. The plot should appear in the window of your read and plot program.

# Conclusion:
We can go upto period=100, but we have a overshoot with 10%, what is too high for the upcoming project.
Better is the period of 60 with around 2,5% overshoot, what should be good and 6 times slower than the orininal value of 10, what gives us more remaining power to do other tasks in the upcoming project.

You can also plug in two different motors and set a desired point and the controller will set their position simultaniously
