temperature = float(input("Enter temperature in °C: "))

if temperature < 15:
    print("Cold")
elif 15 <= temperature <= 30:
    print("Normal")
else:
    print("Hot")
