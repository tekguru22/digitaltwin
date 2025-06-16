import random

def generate_nibp():
    sys = random.randint(110, 130)
    dia = random.randint(70, 85)
    return sys, dia

def generate_temperature():
    return round(random.uniform(36.0, 37.5), 1)
