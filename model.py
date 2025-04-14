from typing import List, Dict, Tuple, Set
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
    # counters
    # probCuisine_givenDay = 0
    # probCuisine_givenDay = 0
    # probCuisine_givenDay = 0
    # probCuisine_givenDay = 0

    SAMPLE = 1000000
    # Identify cuisines with at least one valid recipe.
    valid_cuisines = {recipe[1] for recipe in valid_recipes}
    cuisine_counts = {cuisine: 0 for cuisine in valid_cuisines}

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
    final_cuisine_probs = {cuisine: count / total_valid for cuisine, count in cuisine_counts.items()}

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
    best_recipes = [name for name, prob in recipe_probabilities.items() if prob == max_prob]

    # Output the winning recipe(s)
    print("Recommended recipe(s):")
    for name in best_recipes:
        print(f"{name} with probability {max_prob:.4f}")


if __name__ == "__main__":
    recipes = [
        # Indian recipes
        ("Chicken Curry", "indian", ["chicken", "onion", "spices"]),
        ("Paneer Tikka", "indian", ["paneer", "yogurt", "spices"]),
        ("Chana Masala", "indian", ["chickpeas", "tomato", "onion", "spices"]),
        ("Lamb Vindaloo", "indian", ["lamb", "potato", "spices", "vinegar"]),

        # Chinese recipes
        ("Sweet and Sour Pork", "chinese", ["pork", "pineapple", "peppers"]),
        ("Kung Pao Chicken", "chinese", ["chicken", "peanuts", "chili", "scallions"]),
        ("Mapo Tofu", "chinese", ["tofu", "ground pork", "chili bean paste", "scallions"]),

        # Japanese recipes
        ("Sushi", "japanese", ["rice", "fish", "seaweed"]),
        ("Ramen", "japanese", ["noodles", "pork", "egg", "scallions"]),
        ("Tempura", "japanese", ["shrimp", "vegetables", "tempura batter"]),
    ]

    # Fridge One:
    # - Indian: "chicken", "onion", "spices" (for Chicken Curry)
    # - Chinese: "pork", "pineapple", "peppers" (for Sweet and Sour Pork)
    # - Japanese: "rice", "fish", "seaweed" (for Sushi)
    fridge_one = [
        ("chicken", "meat", 2),
        ("onion", "vegetable", 5),
        ("spices", "condiment", 3),
        ("pork", "meat", 3),
        ("pineapple", "fruit", 1),
        ("peppers", "vegetable", 3),
        ("rice", "grain", 5),
        ("fish", "seafood", 3),
        ("seaweed", "vegetable", 2),
    ]

    # Fridge Two:
    # - Indian: "chickpeas", "tomato", "onion", "spices" (for Chana Masala)
    # - Chinese: "chicken", "peanuts", "chili", "scallions" (for Kung Pao Chicken)
    # - Japanese: "noodles", "pork", "egg", "scallions" (for Ramen)
    fridge_two = [
        ("chickpeas", "legume", 4),
        ("tomato", "vegetable", 3),
        ("onion", "vegetable", 5),
        ("spices", "condiment", 3),
        ("chicken", "meat", 2),
        ("peanuts", "nut", 2),
        ("chili", "vegetable", 3),
        ("scallions", "vegetable", 4),
        ("noodles", "grain", 3),
        ("pork", "meat", 2),
        ("egg", "dairy", 4),
    ]

    # Fridge Three:
    # - Indian: "paneer", "yogurt", "spices" (for Paneer Tikka)
    # - Chinese: "tofu", "ground pork", "chili bean paste", "scallions" (for Mapo Tofu)
    # - Japanese: "shrimp", "vegetables", "tempura batter" (for Tempura)
    fridge_three = [
        ("paneer", "dairy", 2),
        ("yogurt", "dairy", 2),
        ("spices", "condiment", 3),
        ("tofu", "soy", 2),
        ("ground pork", "meat", 1),
        ("chili bean paste", "condiment", 1),
        ("scallions", "vegetable", 4),
        ("shrimp", "seafood", 2),
        ("vegetables", "vegetable", 5),
        ("tempura batter", "baking", 1),
    ]

    valid_one = get_valid_recipes(recipes, fridge_one)
    valid_two = get_valid_recipes(recipes, fridge_two)
    valid_three = get_valid_recipes(recipes, fridge_three)

    print("For Fridge One (Monday):")
    calculate_cuisine_probabilities(valid_one, prior[MONDAY])
    print("\nFor Fridge Two (Tuesday):")
    calculate_cuisine_probabilities(valid_two, prior[TUESDAY])
    print("\nFor Fridge Three (Wednesday):")
    calculate_cuisine_probabilities(valid_three, prior[WEDNESDAY])

# def bayesian_sampling(samples):
#     # init counters
#     countD_givenA = 0
#     countA_givenD = 0
#     countD = 0
#     countA = 0
#
#     for i in range(samples):
#         # set A, P(+A) = 0.1, P(-A) = 0.9
#         a = '+A' if random.random() < 0.1 else '-A'
#
#         # set b given a
#         # P(+B | +A) = 0.3, P(-B | +A) = 0.7
#         if a == '+A':
#             b = '+B' if random.random() < 0.3 else '-B'
#
#         # P(+B | -A) = 0.5, P(-B | -A) = 0.5
#         else:
#             b = '+B' if random.random() < 0.5 else '-B'
#
#         # setting c given a and b
#         # P(+C | +A, +B) = 0.2, P(-C | +A, +B) = 0.8
#         if a == '+A' and b == '+B':
#             c = '+C' if random.random() < 0.2 else '-C'
#
#         # P(+C | +A, -B) = 0.4, P(-C | +A, -B) = 0.6, 
#         elif a == '+A' and b == '-B':
#             c = '+C' if random.random() < 0.4 else '-C'
#             
#         # P(+C | -A, +B) = 0.6, P(-C | -A, +B) = 0.4, 
#         elif a == '-A' and b == '+B':
#             c = '+C' if random.random() < 0.6 else '-C'
#
#         # P(+C | -A, +B) = 0.8, P(-C | -A, -B) = 0.2, 
#         else:
#             c = '+C' if random.random() < 0.8 else '-C'
#
#
#         # set d given c
#         # P(+D | +C) = 0.7, P(-D | +C) = 0.3
#         if c == '+C':
#             d = '+D' if random.random() < 0.7 else '-D'
#
#         # P(+D | -C) = 0.9, P(-D | -C) = 0.1
#         else:
#             d = '+D' if random.random() < 0.9 else '-D'
#
#
#         # update counters for sampling
#         # P(+D | +A)
#         if a == '+A':
#             countA += 1
#             if d == '+D':
#                 countD_givenA += 1
#
#         # P(+A | +D)
#         if d == '+D':
#             countD += 1
#             if a == '+A':
#                 countA_givenD += 1
#
#
#     # calculate probability, countX given Y over total Y
#     probabilityD_givenA = countD_givenA / countA
#     probabilityA_givenD = countA_givenD / countD
#
#     return probabilityD_givenA, probabilityA_givenD
#

# example pseudocode
# # check the fridge, for each recipe that matches the ingredients COMPLETELY, add to a valid recipe list
# valid_list = []
#
# for each_recipe in fridge_number:
#     # for every item in the fridge
#     for i in range(len(ingredients)):
#         # get valid recipes, add to our valid_list
#
#     # run bayesian sampling on all recipes, based on the prior, then create an output based on our probability calculations
#
#
# # prior
# user has liked indian 50%, chinese 25%, japanese 25% on monday #type:ignore
#
