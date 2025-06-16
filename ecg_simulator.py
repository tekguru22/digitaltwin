import numpy as np

def generate_ecg(heart_rate=75):
    t = np.linspace(0, 1, 500)
    freq = heart_rate / 60  # convert bpm to Hz
    ecg_wave = 0.6 * np.sin(2 * np.pi * freq * t) + 0.2 * np.sin(2 * np.pi * 50 * t)
    noise = 0.05 * np.random.randn(len(t))
    return ecg_wave + noise
