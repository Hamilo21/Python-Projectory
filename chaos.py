# File: chaos.py
# Created 11/13/18 by Logan Hamilton
# A simple program illustrating chaotic behavior.


def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1"))
    for i in range(20) :
        x = 3.9 * x * (1 - x)
        print(x)
main() 
x = 2.0 * x * (1 - x)
20 = eval(input(" How many numbers should I print? ”))

