print("The Cave 🗻")
print("Can you find the legendary treasure? 💎\n")
health = int(input("Enter your health (0-100): "))
energy = int(input("Enter your energy (0-100): "))
has_sword = input("Do you have a sword? (y or n): ").strip().lower()
print("\nYou enter a dark, damp cave. It's eerily silent...")

if health > 70:
    print("You're feeling health! You venture deeper intor the cave...")
    if energy > 50:
        # Evaluation health and energy
        print("You have plenty of energy to fight off any threats!")
    else:
        print("You feel a bit tired but can still press on")
else:
    print("You feel weak... this might be the end...")        

    # Evaluating do we have a sword????
    if has_sword == "y":
        print("\n Suddenly, a wild ogre appears!")
        print("You unsheathe the sword, ready to fight!")
    else:
        print("\n👹 30Suddenly, a wild ogre appears!")
        print("You have no weapon! This could be trouble...")
    print("\nThe ogre roars and charges at you!")
    if health > 30 and (has_sword == "y" or energy > 40):
        health -= 50

print("\nAfter more exploring, you find the legendary treasure chest!")
have_key = input(
                "The chest is locked. Do you have a key? (y or n): "
           ).strip().lower() == "y"
if have_key and (health > 10 or energy > 30):
    print("\nYou unlock the chest and find a fortune in gold and jewels! 💎")
    print("🎉 Congratulations! You've found the treasure!")
else:
    print("\nYou can't open the chest.")
    if not have_key:
        print(
            "Without a key, it will never be opened. " 
            "You leave the cave in shame..."
        )
    else:
        print(
            "You have a key, but alas, you are too weak to open the chest " 
            "and claim the bounty for yourself.  Depressing... 😢"
        )
print("\nThanks for playing The Cave! 🗻")