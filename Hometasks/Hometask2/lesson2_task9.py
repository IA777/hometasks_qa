var_1 = 37
var_2 = 99
x = [var_1, var_2]
var_1 = x[1]
var_2 = x[0]
print(var_1)
print(var_2)


var_1 = 37
var_2 = 99
var_1, var_2 = var_2, var_1
print("var_1 =", var_1, "var_2 =", var_2)