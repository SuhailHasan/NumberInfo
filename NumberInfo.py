from phonenumbers import carrier, geocoder
import phonenumbers

print("""
    _   __                __             ____      ____    
   / | / /_  ______ ___  / /_  ___  ____/  _/___  / __/___ 
  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/ // __ \/ /_/ __ \
 / /|  / /_/ / / / / / / /_/ /  __/ / _/ // / / / __/ /_/ /
/_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/ /___/_/ /_/_/  \____/ 
                                                           
                                                    (Made by Suhail)
""")
phoneNo = input("Enter Phone Number: ")
ph =phonenumbers.parse(f"phoneNo")
vn = carrier.name_for_valid_number(ph,"en")
geo = geocoder.description_for_number(ph,"en")
print(vn)
print(geo)
