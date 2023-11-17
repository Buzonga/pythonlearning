primarchs = ['Lion', "Fulgrim", "Perturabo", "Jaghatai Khan", "Leman Russ", "Rogal Dorn", "Konrad Curze", "Sanguinius"
                 , "Ferrus Manus", "Angron", "Roboute Guilliman", "Mortarion", "Magnus the Red", "Horus Lupercal",
                 "Lorgar Aurelian", "Vulkan", "Corvus Corax", ]
print(primarchs[0])

primarchs[0] = "Lion El'Jonson"
print(primarchs)

primarchs.append("Alpharius Omegon")
print(primarchs)

primarchs.insert(1, "2")
primarchs.insert(10, "11")
print(primarchs)

del primarchs[1]
print(primarchs)

primarchs.pop(9)
print(primarchs)

primarchs.remove("Ferrus Manus")
print(primarchs)

primarchs.sort()
print(primarchs)

primarchs.reverse()
print(primarchs)

print(sorted(primarchs, reverse = True))

print(len(primarchs))