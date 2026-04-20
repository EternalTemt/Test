import r2r_dac as r2r
import signal_generator_1 as sg
import time
import RPi.GPIO as GPIO 

amplitude = 3.2
signal_frequency = 1
sampling_frequency = 400
t=0
try:
    dac = r2r.R2R_DAC([16,20,21,25,2,17,27,22],3.2,True)
    dac_b = [16,20,21,25,2,17,27,22]
    while True:
        try:
            voltage = sg.get_sin_wave_amplitude(signal_frequency, t)
            print(voltage)
            dac.set_voltage(voltage * amplitude)
            for i in range(8):
                GPIO.output(dac_b[i],((dac.set_number(dac.set_voltage(voltage * amplitude))))[i])
            sg.wait_For_sampling_period(sampling_frequency)
            t =time.time()
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз")
finally:
    dac.deinit()