import sys


if len(sys.argv) != 2:
    print("Usage: python temperature_check.py <temperature_in_Celsius>")
    sys.exit(1)

temperature = float(sys.argv[1])

if temperature < 15:
    print("Cold")
elif 15 <= temperature <= 30:
    print("Normal")
else:
    print("Hot")

