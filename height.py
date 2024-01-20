# Nested interactive loop
heights=[]# Empty List

while True:
    x=float(input())
    if(x<=0):
        break
    heights.append(x)#this is in inches
output=[x*2.54 for x in heights]
print(output)#this is in cm
