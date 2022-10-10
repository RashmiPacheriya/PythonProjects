#Write a python program to find whether a given username contains less than 10 characters or not.
name = input("Enter your name:")
if(len(name)<10):
    print("Your username is Correct ")
else:
    print("Your username is too long")
