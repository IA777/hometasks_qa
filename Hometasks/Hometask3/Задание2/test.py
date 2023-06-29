class Smartphone:

    def __init__(self, brand, model, num):
        print("Марка телефона: ", brand)
        print("Модель телефона: ",model)
        print("Номер телефона: ", num)

   

my_phone = Smartphone("Samsung", "A10", "+37124860889")
#my_phone.brandIs()


class Smartphone:
    def __init__(self, brand, model, num):
        self.ph_brand = brand
        self.ph_mod = model
        self.ph_num = num

    def brandIs(self):
        print("Марка телефона: ", self.ph_brand)
        print("Модель телефона: ", self.ph_mod)
        print("Номер телефона: ", self.ph_num)

def modIs(self):
    #print("Модель телефона: ", self.modIs)

def numIs(self):
    print("Номер телефона: ", self.numIs) 

my_phone = Smartphone("Samsung", "A10", "+37124860889")
my_phone.brandIs()