from address import Address
from mailing import Mailing

to_address = Address("Riga", "Jasmuizas street", "12", "12", "LV1021" )
from_address = Address("Riga", "Biezina steret", "4", "68", "LV1029")

send_to = Mailing(to_address, from_address, 'LV1327461453', 25)

print(f'Letter number {send_to.track}, is sent from: {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house_num}-{to_address.apart_num}, to index {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house_num}-{from_address.apart_num}. Total price: {send_to.cost} Euro')

