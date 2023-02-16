# lab3
ME-405-03-2232 lab3
SOME README FILE

We can go upto period=100. We have a lil more overshoot with 10%
better is period of 60 with around 2,5%, what should be good and 6 times slower than the orininal value of 10


![alt text](https://github.com/tobsenthomas2/lab3/blob/main/FigurePeriodsTill60.png)
![alt text](https://github.com/tobsenthomas2/lab3/blob/main/PlotPeriodsTill200.png)



To use this motor controller, run the main function and input the desired angle (in encoder ticks), and the desired Kp value. Depending on your motor this value may have to be adjusted. Plotting the step response can help to see if your Kp value is making your system under or over damped. To plot the response, run the readAndPlotOnPC.py program, with your computer attached to the ST-LINK on the micro controller. Ensure that the port is set to the correct USB terminal on your computer. This is in addition to the cable you have set up to run micropython on the micro controller. Now run the main program and wait for the motion to stop. The plot should appear in the window of your read and plot program.

For the motors we used, we found a kp value 0.0265 created the best response from the motors. As seen in image Overshoot4776.png, with a too large kp value, the motor overshoots very much, causing the system to oscilate back and forth without coming to a stop. As seen in image Undershoot47912.png, with too low of a kp value it takes over a whole second to reach the desired position. The kp can be adjusted back and forth using this plotting software in order to find the perfect kp value for your motor.
