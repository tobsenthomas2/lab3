#Motor 1 initialization set up
from PWM_Calc import PWM_Calc
import pyb, time
from encoder_reader import EncoderClass
from  motor_driver import MotorDriver

def Motor1(reset):
    state = 0
    while True:
        if state == 0:
            Motor1=MotorDriver(pyb.Pin.board.PA10,pyb.Pin.board.PB4,pyb.Pin.board.PB5,3)
            encoder1=EncoderClass(pyb.Pin.board.PB6,pyb.Pin.board.PB7,4)
            encoder1.zero()
            time_step = 0.01
            Theta_Set = 100000
            KP = 0.01
            count = 0
            pwm1 = PWM_Calc()
            pwm1.set_setpoint(Theta_Set)
            pwm1.set_KP(KP)
            state = 1
            yield state
            
        elif state == 1:
            Theta_Act = encoder1.read()
            PWM = pwm1.Run(Theta_Act)
            Motor1.set_duty_cycle(PWM)
            time.sleep(time_step) #updates 0.01s
            count += 1
            
            if count == 400:
                state = 2
            yield state
            
        elif state == 2:
            Motor1.set_duty_cycle(0)
            pwm1.Print_Data(False)
            state = 3
            
            yield state
            
        elif state == 3:
            if reset == True:
                state = 0
            yield state
