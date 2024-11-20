# Lists (Arrays)
inventory = ["wand", "invisibility cloak", "maruader's map", "broomstick"]

print(f"First item: {inventory[0]}")
print(f"Third item: {inventory[2]}")
print(f"Last item: {inventory[-1]}")
            
# Mixed lists and adding items
inventory.append(9.75) # adds it to the end of the list
inventory.append("golden snitch")
print(f"\nAdded 9.75 and then golden snitch to the end: {inventory}")
inventory.insert(2, "howler letter") # places this in the index of 2 (3rd)
print(f"\nAdded howler letter at position 2: {inventory}")

# Removing items
inventory.remove("invisibility cloak")
print(f"\nRemoved invisibility cloak: {inventory}")

del inventory[1]
print(f"\nDeleted item at index 1: {inventory}") 
# del is a global function and .remove is on a specific item
# Removing and retrieving the last item with pop()
last_item = inventory.pop()
print((f"\nPopped the last item: {last_item}"))
print(f"\nInventory after pop: {inventory}")

# Extending the inventory with more magical items
more_items = ["philosopher's stone", "butter beer"]
inventory.extend(more_items) # combines lists
print(f"\nExtended inventory: {inventory}")

# Slicing
print(f"\nFirst three items: {inventory[:3]}")
print(f"\nLast two items: {inventory[-2]}")
print(f"\n2nd and 3rd items: {inventory[1:3]}")

# Nested lists 
inventory.append(["expelliarmus", "expecto patronum", "lumos"])
print(f"\nAdded spell list: {inventory}")
print(f"First spell: {inventory[6][0]}")
print(f"Third spell: {inventory[-1][2]}")

inventory.append(["Elder Wand", "Time Turner", "Horcrux", "Floo Powder"])
print(f"\nAdded more items list: {inventory}")
print(f"Second item: {inventory[7][1]}")
print(f"Third item: {inventory[7][2]}")

# Finding the length of a list
print(f"\nTotal items in inventory: {len(inventory)}")

# Looping through the inventory list
print("\nLooping through Harry's inventory:")
for item in inventory:
    print(f"- {item}")

print("\nLooping through every item of Harry's inventory:")
for item in inventory: # for loop item temporary variable exists in loop
    if isinstance(item, list):
        for nested_item in item:
            print(f"- {nested_item}")

    else:
        print(f"- {item}")

# Clearing the inventory
inventory.clear()
print(f"\nInventory cleared: {inventory}")

# Numeric operations on a list of potion  (fictional)
potion_quantities = [7, 12, 3, 5]
print(f"\nMin potion quantity: {min(potion_quantities)}")
print(f"Max potion quantity: {max(potion_quantities)}")


# Sorting and reversing position quantities
potion_quantities.sort()
print(f"\nSorted potion quantities: {potion_quantities}")
potion_quantities.reverse()
print(f"Reversed sorted potion quantities: {potion_quantities}")


def greet(Greg, Daniel):
    return(f"Well, hello {Greg} and {Daniel}.")