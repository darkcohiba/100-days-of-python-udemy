name = input("What is your name: \n")
print(f"Hello {name}!")
print("Welcome to Treasure Island.")
print("My name is dobbins and I will be accompanying you along your journey!")
print("Our mission is to find the treasure.")
first_turn = input("You are at a crossroads... Should we go left or right? \n")
if first_turn == "left":
    swim = input("We are at a small river crossing, we notice a small dock up ahead. Should we wait or swim across? swim or wait? \n")
    if swim == "swim":
        print(f"A sea snake jumps out of the water, his tail whips back. The sudden crack slices through {name}'s arm leaving him gushing blood. Dobbins swam back and escaped to safety as {name} drowned deep into the ocean... game over...")
    else:
        print("As you approach the dock, the boat keeper comes out from the fog. \n Dobbins walks up to him and asks about passage across the river. He gestures you.")
        boat = input("As you walk slowly towards him you can feel the air thicken and the stench of the alcohol on his collar grew stronger. Dobbins looks up at you and says 'he can give us passage for a fee, should we do it?', you reluctantly look down at Dobbins and say... 'yes' or 'no'")
        if boat == "yes":
            print("You get on the rickety boat and make it across the water safely.")
        else:
            print("As you tell the boat keeper no a gigantic spider approaches from behind quickly casting a web around Dobbins and you. Your trapped in his web and slowly fade off into the darkness...death is upon you...game over.")
else:
    print("Sadly a group alligators was hidden in the bushes and jumped out the second we turned right. Game Over...")
