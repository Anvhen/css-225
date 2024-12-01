
import random

def search_wreckage():
    """Search the wreckage for supplies."""
    supplies = ["tools", "food", "distress beacon"]
    found_item = random.choice(supplies)
    print(f"You find a {found_item} in the wreckage.")
    return found_item

def explore_area():
    """Explore the surrounding area to gather information."""
    creatures = ["local creature", "unusual plant", "ancient artifact"]
    found_creature = random.choice(creatures)
    print(f"You encounter a {found_creature} while exploring.")
    return found_creature

def set_up_camp():
    """Set up a temporary camp and rest to recover health."""
    print("You set up a camp and rest to recover your health.")
    health_recovery = 20  # Example health points recovered
    return health_recovery

def head_north():
    """Decide to head north toward a distant mountain."""
    print("You decide to head north toward the distant mountain.")
    # Proceed to Chapter 2
