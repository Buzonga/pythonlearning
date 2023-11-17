clients = input("How many people are in your diner group? ")
clients = int(clients)

if clients > 8:
    print("Sorry, you will need to wait for a table.")
else:
    print("Your table is ready.")