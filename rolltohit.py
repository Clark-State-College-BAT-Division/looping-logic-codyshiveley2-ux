#This simulates rolling to hit in Warhammer 40,000
#Prompt the user how many dice are being rolled, and what the hit target is
#Roll the correct number of dice, then display the results
#This is a guided practice. Either follow with the video or your instructor will
#go over this in class.

import random

print("Warhammer 40,000 Hit Roll Simulator")


num_dice = int(input("How many dice are being rolled? "))


target = int(input("What is the hit target (e.g., 3 means 3+)? "))


rolls = []
for _ in range(num_dice):
    roll = random.randint(1, 6)
    rolls.append(roll)


print("\nResults:")
for i, roll in enumerate(rolls, start=1):
    outcome = "HIT" if roll >= target else "MISS"
    print(f"Die {i}: rolled a {roll} → {outcome}")


hits = sum(1 for r in rolls if r >= target)
print(f"\nTotal hits: {hits} out of {num_dice}")
