digit = int(input("Enter a digit: "))

for i in range(digit):
    if i < digit - 1:
        print(2 * i + 1, end=", ")
    else:
        print(2 * i + 1, end="")

