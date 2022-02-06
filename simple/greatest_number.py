
def greatest_number(*args):

    highest = 0
    for i in args:
        if highest < i:
            highest == i

    return highest

if __name__ == "__main__":

    a = int(input("enter the number: "))
    b = int(input("enter the number2: "))
    c = int(input("enter the number3: "))

    print("the greatest number is", greatest_number(a, b, c))