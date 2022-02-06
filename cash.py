from cs50 import get_float

# Getting input from user
cash = 0
while(cash <= 0):
    cash = get_float("Change owed: ")

# Concerting to 100's
cash = cash*100
change = [25, 10, 5, 1]

# Applying the greedy algorithm
i = 0
out = 0
while(cash != 0):
    while(cash < change[i]):
        i + 1
    cash -= change[i]
    out += 1

# Printing the output
print(out)