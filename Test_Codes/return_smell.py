def check_temperature(temp):
    if temp < 0:
        return "Extremely Cold"
    if temp >= 0 and temp < 5:
        return "Very Cold"
    if temp >= 5 and temp < 10:
        return "Cold"
    if temp >= 10 and temp < 15:
        return "Mild"
    if temp >= 15 and temp < 20:
        return "Warm"
    if temp >= 20 and temp < 25:
        return "Very Warm"
    if temp >= 25 and temp < 30:
        return "Hot"
    if temp >= 30 and temp < 35:
        return "Very Hot"
    if temp >= 35:
        return "Extremely Hot"
    return "Unknown"

print(check_temperature(18))  # Prints "Warm"
