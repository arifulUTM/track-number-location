import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+880")
phone_number2 = phonenumbers.parse("+60")

print(geocoder.description_for_number(phone_number1,'en'))
print(geocoder.description_for_number(phone_number2,'en')) 


#pip install phonenumbers
#dont forget to install this eenjoy

