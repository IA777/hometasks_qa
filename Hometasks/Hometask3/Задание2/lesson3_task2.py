from smartphone_model import Smartphone

catalog = []

smart_1 = Smartphone("Samsung", "A10", "+37124860889")
catalog.append(smart_1)

smart_2 = Smartphone("Nokia", "3310", "+49454688221")
catalog.append(smart_2)

smart_3 = Smartphone("Ericksson", "T28s", "+790522555445")
catalog.append(smart_3)

smart_4 = Smartphone("Apple", "4s", "+37028556674")
catalog.append(smart_4)

smart_5 = Smartphone("One Plus", "One", "+86266579855")
catalog.append(smart_5)

    

print("Каталог телефонов:")
for phone in catalog:
    print(f"{phone.ph_brand} - {phone.ph_mod} - {phone.ph_num}")

