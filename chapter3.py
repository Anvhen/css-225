
def investigate_technology():
    """Investigate ancient technology for ship repairs."""
    technology = ["power core", "navigation module", "energy crystals"]
    found_technology = random.choice(technology)
    print(f"You uncover a piece of advanced technology: {found_technology}. It may help repair your ship.")
    return found_technology

def solve_puzzle():
    """Solve a puzzle to unlock a secret."""
    puzzle_difficulty = random.choice(["easy", "medium", "hard"])
    print(f"You encounter a puzzle. Difficulty: {puzzle_difficulty}")
    success = random.choice([True, False])
    if success:
        print("You solve the puzzle and uncover a secret!")
        return True
    else:
        print("The puzzle is too difficult. You fail and suffer damage!")
        return False

def avoid_traps():
    """Avoid traps in the ruins."""
    traps = ["poison dart", "pitfall", "spike trap"]
    encountered_trap = random.choice(traps)
    print(f"You trigger a trap: {encountered_trap}. You need to act quickly!")
    success = random.choice([True, False])
    if success:
        print("You manage to avoid the trap!")
        return True
    else:
        print("You fall into the trap and lose health.")
        return False

def decide_return_or_explore():
    """Decide whether to return to the Zyren village or go deeper into the ruins."""
    decision = input("Do you want to return to the Zyren village or go deeper into the ruins? (return/deeper): ")
    if decision.lower() == "return":
        print("You decide to return to the Zyren village for safety.")
        return "return"
    else:
        print("You decide to go deeper into the ruins.")
        return "deeper"
