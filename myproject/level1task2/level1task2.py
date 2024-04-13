## temperature conversion ##
u=input("Is the temperture is in Celsius or Farenheat (C/F): ")
t=float(input("Enter the temperature:  "))
if u=="C":
    m=(t*1.8)+32
    print("The temperature is:",m)
elif u=="F":
    r=((t-32)*5)/9
    print("The temperature is:",r)
else:
    print("Invalid input")

