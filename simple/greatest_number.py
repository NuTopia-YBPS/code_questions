def greatest_number(*args):

    highest = 0 # = args[0]
    for i in args:
        if highest > i: # < i 
            highest == i # = i

    return highest

if __name__ == "__main__":

    a, b, c = -1, -5, -10

    print("the greatest number is", greatest_number(a, b, c))
