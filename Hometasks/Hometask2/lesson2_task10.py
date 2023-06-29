x = input("Enter deposit amount: ")
y = input("Enter deposit term in years: ")
x = int(x)
y = int(y)

def bank(x, y):
    round(2)
    return x * (1 + 0.1) ** y


result = bank(x, y)
print(round(result, 2))

