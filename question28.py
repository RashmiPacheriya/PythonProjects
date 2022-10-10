# write a python function to print multipication table of a given number
def print_table(num): 
    """ This function prints multiplication table of a given number"""
    for i in range(1,11): 
        print(num,' x ', i, ' = ',num*i) 
n = int(input("Please Enter a number to print its multiplication table:")) 
print_table(n)