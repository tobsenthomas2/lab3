import pyb, time
             
class EncoderClass:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """
    def __init__ (self, in1pin, in2pin, timerNR):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several pin parameters)
        In1pin and In2pin are used to define the pins (B6/B7 or C6/C7). 
        TimerNR sets the timer channel based on the pins (TCh 4 or 8)                                                                 
           
        """
        self.IN1_Pin=in1pin
        self.IN2_Pin=in2pin
        self.counterTimer=timerNR
        #self.deltaTime=
        self.totalPos=0
        self.prevCount=0
        self.threshold=30000
        
        
        """!This sets encoder channels A and B to recieve data from Pyb, for
        In1 and In2 pins which can be set based on the specific pins, and
        motors being used
        """

                                                    

        enc_chA = pyb.Pin(self.IN1_Pin, pyb.Pin.IN)

        enc_chB = pyb.Pin (self.IN2_Pin, pyb.Pin.IN)
        """!Enables the timer to count w/ a prescaler of 0 and a period
        or range of values from 0 to hex FFFF, and allows for the Timer channel
        to be specified
        
        Sets ch1 to timer channel 1  to read A&B for encoder A corresponding to channel A
        which is the same for ch2
        """
                                                                        
        timer= pyb.Timer (self.counterTimer, prescaler=0, period=0xFFFF)
        ch1=timer.channel (1, pyb.Timer.ENC_AB, pin=enc_chA)
        ch2=timer.channel (2, pyb.Timer.ENC_AB, pin=enc_chB)
        self.counter=timer
        
        print ("Creating a motor driver")

    def read (self):
        """!
        This method checks the counter value - the previous counter value
        and comparing it to our "threshold". This checks for overflow.
        If less than the threshold, we assume this is counting up and has overflowed.
        We can scale this properly and vice versa for counting down.
                                                      
                                                      
        """
        #print("counter " +str(self.counter.counter())+"totalPos " +str(self.totalPos)+" for encoderTim: " +str(self.counterTimer))
        if (self.counter.counter()-self.prevCount <-self.threshold):
            self.totalPos+=self.counter.counter()-self.prevCount+65535
        elif (self.counter.counter()-self.prevCount > self.threshold):
            self.totalPos+=self.counter.counter()-self.prevCount-65535          
        else:
            self.totalPos+=self.counter.counter()-self.prevCount
            
        
        self.prevCount=self.counter.counter()
        return self.counter.counter()
        
    def zero(self):
        """!
        This method zeroes our counter value: our readable counter value
        is self.counter, using the .counter(0) we can reset this value
        and also reset the total position to 0
        """
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        print("reset counter to 0")
        self.counter.counter(0)
        self.totalPos=0
        
# 
# class EncoderClass:
#     """! 
#     This class implements a motor driver for an ME405 kit. 
#     """
#     threshold=30000
# 
#     def __init__ (self, in1pin, in2pin, timerNR):
#         """! 
#         Creates a motor driver by initializing GPIO
#         pins and turning off the motor for safety. 
#         @param en_pin (There will be several pin parameters)
#         In1pin and In2pin are used to define the pins (B6/B7 or C6/C7). 
#         TimerNR sets the timer channel based on the pins (TCh 4 or 8)
#         """
#         self.IN1_Pin=in1pin
#         self.IN2_Pin=in2pin
#         self.counterTimer=timerNR
#         #self.totalPos
#         self.prevCount=0
#         
#         
#         """!This sets encoder channels A and B to recieve data from Pyb, for
#         In1 and In2 pins which can be set based on the specific pins, and
#         motors being used
#         """
#         enc_chA = pyb.Pin(self.IN1_Pin, pyb.Pin.IN)
#         enc_chB = pyb.Pin(self.IN2_Pin, pyb.Pin.IN)
# 
#         """!Enables the timer to count w/ a prescaler of 0 and a period
#         or range of values from 0 to hex FFFF, and allows for the Timer channel
#         to be specified
#         
#         Sets ch1 to timer channel 1  to read A&B for encoder A corresponding to channel A
#         which is the same for ch2
#         """
#         timer= pyb.Timer (self.counterTimer, prescaler=0, period=0xFFFF)
#         ch1=timer.channel (1, pyb.Timer.ENC_AB, pin=enc_chA)
#         ch2=timer.channel (2, pyb.Timer.ENC_AB, pin=enc_chB)
#         self.counter=timer
#         
#         print ("Creating a motor driver")
# 
#     def read (self):
#         """!
#         This method checks the counter value - the previous counter value
#         and comparing it to our "threshold". This checks for overflow.
#         If less than the threshold, we assume this is counting up and has overflowed.
#         We can scale this properly and vice versa for counting down.
#         """
#         #print("counter " +str(self.counter.counter())+" for encoderTim: " +str(self.counterTimer))
#         if (self.counter.counter()-self.prevCount <-threshold):
#             self.totalPos+=self.counter.counter()-self.prevCount+65535
#         elif (self.counter.counter()-self.prevCount > threshold):
#             self.totalPos+=self.counter.counter()-self.prevCount-65535          
#         else:
#             self.totalPos+=self.counter.counter()-self.prevCount
#             
#         
#         self.prevCount=self.counter.counter()
#         
#         return self.counter.counter()
#     def zero(self):
#         """!
#         This method zeroes our counter value: our readable counter value
#         is self.counter, using the .counter(0) we can reset this value
#         and also reset the total position to 0
#         """
#         print("reset counter to 0")
#         self.counter.counter(0)
#         self.totalPos=0
#         
#         
#         
# #         
# #         
# # if __name__ == "__main__":
# #     encoder=EncoderClass(pyb. Pin.board. PB6,pyb. Pin.board. PB7,4)
# #     while(1):
# #          encoder.read()
# #          time.sleep(0.5)