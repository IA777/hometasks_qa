year = input("ВВедите год: ")  
year = int(year)
def is_year_leap(year):
    if year % 4 == 0:
        print("Год", year, "является виокосным")
       
    else:
        print("Год", year, "не является високосным")


is_year_leap(year)


