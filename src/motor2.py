#Motor 1 initialization set up

from PWM_Calc import PWM_Calc
import pyb, time
from encoder_reader import EncoderClass
from  motor_driver import MotorDriver


def Motor2(reset):
    state = 0
    while True:
        if state == 0:
            Motor2=MotorDriver(pyb.Pin.board.PC1,pyb.Pin.board.PA0,pyb.Pin.board.PA1,5)
            encoder2=EncoderClass(pyb.Pin.board.PC6,pyb.Pin.board.PC7,8)
            encoder2.zero()
            time_step = 0.01
            Theta_Set = 100000
            KP = 0.025
            count = 0
            pwm2 = PWM_Calc()
            pwm2.set_setpoint(Theta_Set)
            pwm2.set_KP(KP)
            state = 1
            yield state
            
        elif state == 1:
            Theta_Act = encoder2.read()
            PWM = pwm2.Run(Theta_Act)
            Motor2.set_duty_cycle(PWM)
            time.sleep(time_step) #updates 0.01s
            count += 1
            
            if count == 400:
                state = 2
            yield state
            
        elif state == 2:
            Motor2.set_duty_cycle(0)
            pwm2.Print_Data(True)
            state = 3
            
            yield state
            
        elif state == 3:
            if reset == True:
                state = 0
            yield state

