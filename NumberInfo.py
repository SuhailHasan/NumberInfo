from phonenumbers import carrier, geocoder
import phonenumbers
phoneNo = input("Enter Phone Number: ")
ph =phonenumbers.parse(f"phoneNo")
vn = carrier.name_for_valid_number(ph,"en")
geo = geocoder.description_for_number(ph,"en")
print(vn)
print(geo)
