X = input("Enter deposit amount: ")
Y = input("Enter deposit term in years: ")
X = int(X)
Y = int(Y)

def bank(X, Y):
    return X * (1 + 0.1) ** Y


result = bank(X, Y)
print(result)

