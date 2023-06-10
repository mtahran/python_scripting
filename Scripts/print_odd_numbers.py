lower_limit = int(input("Enter the lower limit for the range:"))
upper_limit = int(input("Enter the upper limit for the range:"))
for j in range(lower_limit, upper_limit + 1):
    if j % 2 != 0:
        print(j)