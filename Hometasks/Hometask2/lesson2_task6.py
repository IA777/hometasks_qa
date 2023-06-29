lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
new_lst = []
for x in range(0, len(lst)):
    if lst[x] < 30 and lst[x] % 3 == 0:
        new_lst.append(lst[x])
    
print(new_lst)     
