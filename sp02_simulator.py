import numpy as np

def generate_spo2_wave():
    t = np.linspace(0, 1, 300)
    wave = 0.4 * np.sin(2 * np.pi * 2 * t) + 0.1 * np.random.randn(len(t))
    return wave
