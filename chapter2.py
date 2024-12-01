
def communicate_with_zyren():
    """Attempt to communicate with the Zyren using a translation device."""
    responses = ["We are the Zyren.", "What is your purpose here?", "You may stay with us."]
    print("You activate your translation device and the Zyren speak to you.")
    return random.choice(responses)

def help_zyren():
    """Offer to help the Zyren with their problem."""
    problems = ["find crystals for ship repairs", "defend the village from a threat"]
    print(f"You offer to help the Zyren to {random.choice(problems)}.")
    success = random.choice([True, False])
    if success:
        print("The Zyren are grateful for your help and trust you.")
        return True
    else:
        print("The Zyren are hesitant. They need more proof of your trustworthiness.")
        return False

def search_for_resources():
    """Search the area for hidden resources (e.g., crystals)."""
    resources = ["crystals", "food supplies", "alien technology"]
    found_resource = random.choice(resources)
    print(f"You find some {found_resource} in the area.")
    return found_resource

def decide_stay_or_continue():
    """Decide whether to stay with the Zyren or continue north."""
    decision = input("Do you want to stay with the Zyren? (y/n): ")
    if decision.lower() == "y":
        print("You decide to stay with the Zyren and help them with their problems.")
        return "stay"
    else:
        print("You decide to continue north toward the ancient ruins.")
        return "continue"
