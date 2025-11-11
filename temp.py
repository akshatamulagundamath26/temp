import sys

# Check if the user has provided the temperature argument
if len(sys.argv) != 2:
    print("Usage: python temperature_check.py <temperature_in_Celsius>")
    sys.exit(1)

# Read temperature from command line
temperature = float(sys.argv[1])

# Check temperature range
if temperature < 15:
    print("Cold")
elif 15 <= temperature <= 30:
    print("Normal")
else:
    print("Hot")

