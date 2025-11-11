import sys

if len(sys.argv) == 2:
    temp = sys.argv[1]      
else:
    temp = "25"           

temp = int(temp)            
print(f"Temperature: {temp}")

if temp < 15:
    print("Cold")
elif temp >= 15 and temp <= 30:
    print("Normal")
else:
    print("Hot")

