#Alpharius 19/09/2023, this program creates a name with the first letter being un uppercase, and puts the name together.

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

#This one is to test some of the methods on the string

name = "Alpharius"
name_lower = name.lower()
name_upper = name.upper()
name_title = name.title()

print(name_lower)
print(name_upper)
print(name_title)