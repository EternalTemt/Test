import numpy as np
import time

def get_sin_wave_amplitude(freq,time):
    phase = 2 *3.14 * freq * time
    res = 1 - 4 * np.abs((phase % 1) - 0.5)
    return (res + 1) / 2

def wait_For_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)