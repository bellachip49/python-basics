# Name: Krystal Kwan
# Date: Tuesday, July 21, 2015
# Topic: Calculating the Perimeter and area of a rectangle and triangle

continuation = "y"

def add():
    global continuation
    try:
        print ("What is the first number?")
        c = int(input("> "))
        print ("What is the second number?")
        d = int(input("> "))
        plus = c + d
        print ("%i + %i = %i" % (c, d, plus))
    except ValueError:
        print ("Oops! That was no valid whole number. Try again...")
        print ("Do you want to continue? Press y for yes and any key to exit.")
        continuation = input("> ")
        return continuation

def sub():
    global continuation
    try:
        print ("What is the first number?")
        a = int(input("> "))
        print ("What is the second number?")
        b = int(input("> "))
        minus = a - b
        print ("%i - %i = %i" % (a, b, minus))
    except ValueError:
        print ("Oops! That was no valid whole number. Try again...")
        print ("Do you want to continue? Press y for yes and any key to exit.")
        continuation = input("> ")
        return continuation

def main():
    while continuation == "y":
        try:
            print ("Please pick an option:")
            print ("\t 1) add")
            print ("\t 2) subtract")
            g = input("> ")
        except KeyboardInterrupt:
            print ("\Quitting")
            break
    if (g == "add") or (g == "1") or (g == "Add"):
        add()
    elif (g == "subtract") or (g == "2") or (g == "Subtract"):
        sub()
    else:
        print("Input Invalid.")


if __name__ == '__main__':
    main()