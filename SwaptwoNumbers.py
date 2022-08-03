# Swap 2 numbers without third vaiable
a = int(input("Enter any integer value for a: "))
b = int(input("Enter any integer value for b: "))
a,b = b,a
print("value of a:",a, " and b:",b)
print("value of a after swap: ", a, " and b after swap: ", b)