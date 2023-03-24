import random
order = []
names = ["Thomas A", "Galen", "Owen"]
for x in range(len(names)):
    new_name = random.choice(names)
    names.remove(new_name)
    order.append(new_name)
print(order)