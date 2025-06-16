import numpy as np

def generate_ecg():
    t = np.linspace(0, 1, 500)
    ecg_wave = 0.6 * np.sin(2 * np.pi * 5 * t) + 0.2 * np.sin(2 * np.pi * 50 * t)
    noise = 0.05 * np.random.randn(len(t))
    return ecg_wave + noise
