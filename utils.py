def predict_status(sys, dia, temp, spo2, hr):
    if sys > 140 or dia > 90:
        return "Hypertension"
    elif sys < 90 or dia < 60:
        return "Hypotension"
    elif temp > 38.5:
        return "Fever"
    elif temp < 35.0:
        return "Hypothermia"
    elif spo2 < 92:
        return "Low Oxygen (Hypoxemia)"
    elif hr > 120:
        return "Tachycardia"
    elif hr < 50:
        return "Bradycardia"
    else:
        return "Healthy"
