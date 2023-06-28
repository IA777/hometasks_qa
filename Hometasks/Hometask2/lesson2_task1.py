def is_year_leap(year):
    if year % 4 == 0:
        print("Год", year, "является виокосным")
       
    else:
        print("Год", year, "не является високосным")

year = 2021  
is_year_leap(year)


