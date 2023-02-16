# lab3
ME-405-03-2232 lab3

# Instruction
The goal of this lab was to test different period times for our motor tasks. The timespan should be as long as possible without seeing a too big decrease in performance. For that we changed the period values manually, then the controller should move the motor to a specific position. After the position has arrived the STM32 sends a data set of the position and time to the PC, where we plot the data and the Maxima to check the overshoot and for discontinuity. The best period we had was 60 ms. Here we had a 2,5% higher value compared to the original period of 10ms. This seems good to us. You can see the dataset in the following plot:
![alt text](https://github.com/tobsenthomas2/lab3/blob/main/FigurePeriodsTill60.png)


We also tried different higher values to see when it is getting really bad. The discontinuity starts at 110 ms, before that only the overshoot is a problem. You can see that in the following Plot:

![alt text](https://github.com/tobsenthomas2/lab3/blob/main/PlotPeriodsTill200.png)


# How to use the programs:

To use this motor controller for two motors, run the main function and input the desired angle (in encoder ticks), and the desired Kp value. Depending on your motor this value may have to be adjusted. To plot the response, run the readAndPlotOnPC.py program, with your computer attached to the ST-LINK on the microcontroller. Ensure that the port is set to the correct USB terminal on your computer. This is in addition to the cable you have set up to run micropython on the microcontroller. Now run the main program and wait for the motion to stop. The plot should appear in the window of your read and plot program.

# Conclusion:
We can go up to period=100, but we have an overshoot of 10%, which is too high for the upcoming project.
Better is the period of 60 with around 2,5% overshoot, which should be good and 6 times slower than the original value of 10, which gives us more remaining power to do other tasks in the upcoming project.

You can also plug in two different motors and set a desired point and the controller will set their position simultaneously
