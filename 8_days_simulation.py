from model import prior, get_valid_recipes, calculate_cuisine_probabilities, user_feedback_loop
from data import fridge_one, fridge_two, fridge_three, recipes

def run_day(day_name: str, day_index: int, fridge: list):
    print(f"\n=== {day_name.upper()} (Day {day_index + 1}) ===")
    print(f"Current Priors: {prior[day_index]}")
    
    valid_recipes = get_valid_recipes(recipes, fridge)
    if not valid_recipes:
        print("No valid recipes for this fridge!")
        return
    
    recipe_probs = calculate_cuisine_probabilities(valid_recipes, prior[day_index])
    if recipe_probs:
        user_feedback_loop(recipe_probs, valid_recipes, prior[day_index])

def main():
    # Make a deep copy of the original priors for comparison
    from copy import deepcopy
    original_prior = deepcopy(prior)
    
    # Simulate 8 days (Monday through next Monday)
    days = [
        ("Monday", 0, fridge_one),
        ("Tuesday", 1, fridge_two),
        ("Wednesday", 2, fridge_three),
        ("Thursday", 3, fridge_one),
        ("Friday", 4, fridge_two),
        ("Saturday", 5, fridge_three),
        ("Sunday", 6, fridge_one),
        ("Next Monday", 0, fridge_two)  # Second Monday to check persistence
    ]
    
    for day_name, day_index, fridge in days:
        run_day(day_name, day_index, fridge)
    
    # Compare original and updated Monday priors
    print("\n=== PRIOR COMPARISON ===")
    print("Original Monday prior:", original_prior[0])
    print("Updated Monday prior:", prior[0])
    
    # Check if the prior changed
    if original_prior[0] != prior[0]:
        print("\nThe Monday prior HAS changed after one week!")
    else:
        print("\nThe Monday prior has NOT changed after one week.")

if __name__ == "__main__":
    main()
