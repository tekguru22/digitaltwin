import numpy as np

def generate_spo2():
    spo2_value = 96 + np.random.randn() * 1.2
    t = np.linspace(0, 1, 300)
    wave = 0.4 * np.sin(2 * np.pi * 2 * t) + 0.1 * np.random.randn(len(t))
    return spo2_value, wave
