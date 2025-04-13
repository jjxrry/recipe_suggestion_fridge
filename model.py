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
    {"indian": 0.5, "chinese": 0.25, "japanese": 0.25},
    {"indian": 0.5, "chinese": 0.25, "japanese": 0.25},
    {"indian": 0.5, "chinese": 0.25, "japanese": 0.25},
    {"indian": 0.5, "chinese": 0.25, "japanese": 0.25},
    {"indian": 0.5, "chinese": 0.25, "japanese": 0.25},
    {"indian": 0.5, "chinese": 0.25, "japanese": 0.25},
]

def get_valid_recipes(recipes: List[Recipe], fridge: Fridge) -> List[Recipe]:
    """Return recipes that can be made with current fridge ingredients."""
    valid_recipes = []
    available_ingredients = {item[0] for item in fridge}
    
    for name, cuisine, ingredients in recipes:
        if all(ingredient in available_ingredients for ingredient in ingredients):
            valid_recipes.append((name, cuisine, ingredients))
    
    return valid_recipes

def calculate_cuisine_probabilities(valid_recipes: List[Recipe], prior: CuisinePrior, prior_given_day: Dict):
    """Calculate adjusted probabilities based on prior preferences and day of week."""
    # TODO:
    # run bayesian sampling based on our priors
    # counters
    # probCuisine_givenDay = 0
    # probCuisine_givenDay = 0
    # probCuisine_givenDay = 0
    # probCuisine_givenDay = 0

    SAMPLE = 1000000
    for i in range(SAMPLE):
        # set indian, P(+indian) = prior_given_day[0], P(-indian) = 1 - prior_given_day[0]


if __name__ == "__main__":
    valid_one = get_valid_recipes(recipes, fridge_one) #type:ignore
    valid_two = get_valid_recipes(recipes, fridge_one) #type:ignore
    valid_three = get_valid_recipes(recipes, fridge_one) #type:ignore

    calculate_cuisine_probabilities(valid_one, prior, prior[MONDAY])
    calculate_cuisine_probabilities(valid_two, prior, prior[MONDAY])

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
