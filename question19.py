#Write a python program to print multiplication table of a given number using while loop
num = int(input("Enter the number: "))
count = 1
while count <= 10:
    num = num * 1
    print(num, '*', count, '=', num * count)
    count += 1