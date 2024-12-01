
def fight_guardian():
    """Choose to fight the guardian robot."""
    print("You choose to fight the guardian robot!")
    strategy = input("Do you want to attack with weapons or use your environment? (weapons/environment): ")
    success = random.choice([True, False])
    if success:
        print("You defeat the guardian robot with your chosen strategy.")
        return True
    else:
        print("The guardian overpowers you. You lose health.")
        return False

def reprogram_guardian():
    """Use technology to reprogram the guardian robot."""
    print("You attempt to reprogram the guardian robot using the ancient technology.")
    success = random.choice([True, False])
    if success:
        print("You successfully reprogram the guardian, turning it into an ally!")
        return True
    else:
        print("The reprogramming fails. The guardian remains hostile.")
        return False

def retreat_to_zyren():
    """Retreat to the Zyren village for assistance."""
    print("You retreat to the Zyren village to regroup and get assistance.")
    return "retreat"

def final_stand():
    """Make a final stand against the guardian robot."""
    print("You make a final stand, risking everything to save the Zyren.")
    success = random.choice([True, False])
    if success:
        print("Your bravery saves the Zyren, and the guardian is defeated.")
        return True
    else:
        print("The guardian overwhelms you. The Zyren are lost.")
        return False
