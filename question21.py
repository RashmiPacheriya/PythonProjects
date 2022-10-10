#Write a python program to find the sum of first n natural numbers using while loop
num = int(input("Enter any Num: "))
total = 0
value = 1
while (value <= num):
    total = total + value
    value = value + 1

print("sum is =",total)