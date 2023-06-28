n = input("Enter month number: ")
n = int(n)
def month_season(n):
    if 1 <= n <= 2 or n == 12:
        print("It is Winter")
    if 3 <= n and n <= 5:
        print("It's Spring") 
    if 6 <= n and n <= 8:
        print("It's Summer")
    if 9 <= n and n <= 11:
        print("It's Autumn")
    if n > 12 or n < 1:
        print("There is no such month")        
month_season(n)