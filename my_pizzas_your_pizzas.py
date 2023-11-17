pizzas = ['4 queijos', 'Calabresa', 'Portuguesa']
friend_pizzas = pizzas[:]

pizzas.append('Pepperoni')
friend_pizzas.append('Marguerita')

print(f'My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print(f"My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)