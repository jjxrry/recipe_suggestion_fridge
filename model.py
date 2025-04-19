from typing import List, Dict, Tuple
import random
from collections import defaultdict

# CONSTANTS:
MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

# TYPE ALIASES
Recipe = Tuple[str, str, List[str]]
FridgeItem = Tuple[str, str, int]
Fridge = List[FridgeItem]
CuisinePrior = List[Dict[str, float]]

# TODO: change these to actual priors
prior: CuisinePrior = [
    {"indian": 0.35, "chinese": 0.45, "japanese": 0.20},  # Monday
    {"indian": 0.25, "chinese": 0.30, "japanese": 0.45},  # Tuesday
    {"indian": 0.50, "chinese": 0.30, "japanese": 0.20},  # Wednesday
    {"indian": 0.30, "chinese": 0.50, "japanese": 0.20},  # Thursday
    {"indian": 0.35, "chinese": 0.35, "japanese": 0.30},  # Friday
    {"indian": 0.45, "chinese": 0.30, "japanese": 0.25},  # Saturday
    {"indian": 0.45, "chinese": 0.30, "japanese": 0.25},  # SUNDAY
]


def get_valid_recipes(recipes: List[Recipe], fridge: Fridge) -> List[Recipe]:
    """Return recipes that can be made with current fridge ingredients."""
    valid_recipes = []
    available_ingredients = {item[0] for item in fridge}

    for name, cuisine, ingredients in recipes:
        if all(ingredient in available_ingredients for ingredient in ingredients):
            valid_recipes.append((name, cuisine, ingredients))

    return valid_recipes


def calculate_cuisine_probabilities(valid_recipes: List[Recipe], prior_given_day: Dict):
    """Calculate adjusted probabilities based on prior preferences and day of week."""
    # TODO:
    # run bayesian sampling based on our priors

    SAMPLE = 1000000
    # Identify cuisines with at least one valid recipe.
    valid_cuisines = {recipe[1] for recipe in valid_recipes}
    cuisine_counts = {cuisine: 0 for cuisine in valid_cuisines}
    # {indian: 0, chinese: 0, japanese: 0}

    # Simulation: Draw cuisines based on the prior and count if valid.
    for _ in range(SAMPLE):
        rand_val = random.random()
        cumulative = 0.0
        chosen_cuisine = None
        for cuisine, prob in prior_given_day.items():
            cumulative += prob
            if rand_val < cumulative:
                chosen_cuisine = cuisine
                break
        if chosen_cuisine in valid_cuisines:
            cuisine_counts[chosen_cuisine] += 1

    # If no valid cuisines were selected, there is nothing to output.
    total_valid = sum(cuisine_counts.values())
    if total_valid == 0:
        print("No valid cuisines were selected in simulation.")
        return

    # Compute adjusted probabilities for each cuisine.
    final_cuisine_probs = {
        cuisine: count / total_valid for cuisine, count in cuisine_counts.items()
    }

    # Group recipes by cuisine.
    recipes_by_cuisine = defaultdict(list)
    for recipe in valid_recipes:
        recipe_name, cuisine, _ = recipe
        recipes_by_cuisine[cuisine].append(recipe_name)

    # Distribute cuisine probability evenly among valid recipes of that cuisine.
    recipe_probabilities = {}
    for cuisine, recipe_names in recipes_by_cuisine.items():
        prob_per_recipe = final_cuisine_probs[cuisine] / len(recipe_names)
        for name in recipe_names:
            recipe_probabilities[name] = prob_per_recipe

    # Identify the highest probability value.
    if not recipe_probabilities:
        print("No recipes to choose from.")
        return

    max_prob = max(recipe_probabilities.values())
    best_recipes = [
        name for name, prob in recipe_probabilities.items() if prob == max_prob
    ]

    # Output the winning recipe(s)
    print("Recommended recipe(s):")
    for name in best_recipes:
        print(f"{name} with probability {max_prob:.4f}")

    return recipe_probabilities


def user_feedback_loop(recipe_probabilities: Dict[str, float], valid_recipes: List[Recipe], prior_day: Dict[str, float]):
    sorted_recipes = sorted(recipe_probabilities.items(), key=lambda x: -x[1])
    print("\nWhich recipe would you like to choose?")
    for idx, (name, prob) in enumerate(sorted_recipes, 1):
        print(f"{idx}. {name} (Prob: {prob:.4f})")

    # Get user's recipe choice
    while True:
        try:
            choice = int(input("Enter the number of your chosen recipe: "))
            if 1 <= choice <= len(sorted_recipes):
                chosen_name = sorted_recipes[choice - 1][0]
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

    # Identify the cuisine of the chosen recipe
    chosen_cuisine = None
    for rname, cuisine, _ in valid_recipes:
        if rname == chosen_name:
            chosen_cuisine = cuisine
            break

    if chosen_cuisine is None:
        print("Cuisine not found. Skipping update.")
        return

    # Ask user to rate the recipe
    while True:
        try:
            rating = float(input(f"You chose a {chosen_cuisine} recipe. Please rate it (0.0 to 1.0): "))
            if 0.0 <= rating <= 1.0:
                break
            else:
                print("Rating must be between 0.0 and 1.0.")
        except ValueError:
            print("Enter a valid float.")

    # Update prior for the selected cuisine based on rating
    learning_rate = 0.1
    old_prior = prior_day[chosen_cuisine]
    prior_day[chosen_cuisine] = old_prior + learning_rate * (rating - old_prior)

    # Normalize the priors to sum to 1
    total = sum(prior_day.values())
    for cuisine in prior_day:
        prior_day[cuisine] /= total

    print(f"Thanks! {chosen_cuisine.capitalize()} prior updated based on your rating.\n")
    print("Updated Prior:")
    for cuisine, prob in prior_day.items():
        print(f"  {cuisine.capitalize()}: {prob:.4f}")

