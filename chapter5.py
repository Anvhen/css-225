
def repair_ship():
    """Repair the ship using gathered resources."""
    resources = ["crystals", "energy cells", "ship parts"]
    gathered_resources = random.choice(resources)
    print(f"You repair the ship using {gathered_resources}.")
    return "ship_repaired"

def decide_escape_or_stay():
    """Decide whether to leave Zyra-5 or stay to help the Zyren."""
    decision = input("Do you want to leave Zyra-5 or stay to help the Zyren? (leave/stay):
