# lab3
ME-405-03-2232 lab3

# Instruction
The goal of this lab was to test different period times for our motor tasks. While in the previous lab our motor was directly controlled in the main program, here we created a task function and utilized a scheduler that would trigger the task to run at a set interval. We adjusted this interval to find the optimal interval that would give us a clean response and take up the least amount of processing time. Using the same target position and kp values, we changed the period that the task ran at and compared the responses. The STM32 sends a data set of the position and time to the PC, where we plot the data and the Maxima to check the overshoot and discontinuity. The best period we had was 60 ms. Here we had only a 2.5% higher maximum value compared to the response using the original period of 10ms. This seems good to us. You can see the dataset in the following plot:
![alt text](https://github.com/tobsenthomas2/lab3/blob/main/FigurePeriodsTill60.png)


We also tried different higher values to see when it starts getting really bad. After about 110ms, there starts to be noticable discontinuity, while below 110ms the main issue is the motor overshooting. You can see that in the following Plot:

![alt text](https://github.com/tobsenthomas2/lab3/blob/main/PlotPeriodsTill200.png)


# How to use the programs:

To use this motor controller for two motors, plug in the micro controller and run the main function. To change the desired position (in encoder ticks) and Kp values, adjust the values in the motor1.py and motor2.py files. Depending on your motor these values may have to be adjusted to not over or undershoot the desired position. To plot the response, run the readAndPlotOnPC.py program, with your computer attached to the ST-LINK on the microcontroller. Ensure that the port is set to the correct USB terminal on your computer. This is in addition to the cable you have set up to run micropython on the microcontroller. Now run the main program and wait for the motion to stop. The plot should appear in the window of your read and plot program. The plot may not correctly register both motors if running at the same time, so do the adjustments for the kp values one at a time.

# Conclusion:
We can go up to period=100, but we have an overshoot of 10%, which is too high for the upcoming project.
We will be using a period of 60 for the future as that only has an overshoot of 2.5%, which should be good enough for our applications. As this is also 6 times slower than the original 10 ms interval it gives us plenty of processing time.
