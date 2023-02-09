import pyb
import time
import utime
#import serial
"""!Supply as an input the setpoint, the desired location of the motor.

Subtract the measured location of the motor from the setpoint; the difference is the error signal, a signed number indicating which way the motor is off and how far.

Multiply the error signal by a control gain called KP to produce a result called the actuation signal. The larger the error, the larger the actuation, so the harder the controller will push. The formula is
\mathrm{PWM} = K_p * (\theta_{setpoint} - \theta_{actual})

Send the actuation signal to the motor driver which you have already written to control the magnitude and direction of motor torque."""
#import matplotlib as
#KP = %/Ticks

class PWM_Calc:
    
    def __init__(self):
        self.KP_set = 0
        self.Theta_Set = 0
        self.time = []
        self.position = []
        self.error = []
        self.pwm = []
        
    def set_KP(self, KP):
        
        self.KP_set = float(KP)
        
    def set_setpoint(self, ThetaSet):
        
        self.Theta_Set = float(ThetaSet)
        
    def Run(self, Theta_Act):
        
        PWM = ((self.Theta_Set - Theta_Act)*self.KP_set)
        
        #PWM needs to be between 0-1 (0*100%)
        
        error = self.Theta_Set - Theta_Act
        
        self.time.append(utime.ticks_ms())
        self.position.append(Theta_Act)
        self.error.append(error)
        self.pwm.append(PWM)
        
        return PWM
    
    def Print_Data(self):
#         for i in range(len(self.time)):
#             print(str(self.time[i]-self.time[0])+","+str(self.position[i]))
            
            

#         with serial.Serial ('COMx', 115200) as s_port:
#             for i in range(len(self.time)):
#                 t = self.time[i]-self.time[0]
#                 x = self.position[i]
#                 s_port.write(f"{t},{x}\r\n")       #Write bytes, not a string
        
        try: 
            u2 = pyb.UART(2, baudrate=115200)      # Set up the second USB-serial port

            for i in range(len(self.time)):
                    t = self.time[i]-self.time[0]
                    x = self.position[i]
                    u2.write(f"{t},{x}\r\n")       #Write bytes, not a string
                
            #flag to tell PC last data point
            u2.write(f"99999,99999\r\n")
            
            #send double for flag2 to tell PC last dataset --> no more plots
            u2.write(f"99999,99999\r\n")
        except:
            print("An exception occurred. Sending Data didnt work")

        
        
        
        
        
        
        #user supplies thetaset, takes thetaact from encoder
        #subtracts and multiplies by KP that we define and outputs the PWM magnitude for MotorDriver()
        
        
    