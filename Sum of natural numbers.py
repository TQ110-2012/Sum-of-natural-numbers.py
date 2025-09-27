from ast import While
from re import I


number = int(input("Enter a number:"))
sum = 0
i = 1
while i<=number:
    sum = sum+i
    i=i+1
print("\nSum=",sum)