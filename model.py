from typing import List, Dict, Tuple, Set
import random
from collections import defaultdict

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

Recipe = Tuple[str, str, List[str]]
FridgeItem = Tuple[str, str, int]
Fridge = List[FridgeItem]
CuisinePrior = List[Dict[str, float]]

def get_valid_recipes(recipes: List[Recipe], fridge: Fridge) -> List[Recipe]:
    """Return recipes that can be made with current fridge ingredients."""
    valid_recipes = []
    available_ingredients = {item[0] for item in fridge}
    
    for name, cuisine, ingredients in recipes:
        if all(ingredient in available_ingredients for ingredient in ingredients):
            valid_recipes.append((name, cuisine, ingredients))
    
    return valid_recipes

def calculate_cuisine_probabilities(valid_recipes: List[Recipe], prior: CuisinePrior, day_of_week: str) -> Dict[str, float]:
    """Calculate adjusted probabilities based on prior preferences and day of week."""
    # TODO:
    # run bayesian sampling based on our priors
    # NOTE: maybe we remove the if name == main function and just do it all here, then call it from that init



if __name__ == "__main__":
    # TODO: change these to actual priors
    prior: CuisinePrior = [
        {"indian": 0.5, "chinese": 0.25, "japanese": 0.25},
        {"indian": 0.5, "chinese": 0.25, "japanese": 0.25},
        {"indian": 0.5, "chinese": 0.25, "japanese": 0.25},
        {"indian": 0.5, "chinese": 0.25, "japanese": 0.25},
        {"indian": 0.5, "chinese": 0.25, "japanese": 0.25},
        {"indian": 0.5, "chinese": 0.25, "japanese": 0.25},
    ]

    # TODO: FIX THIS
    # run this for every day
    # for each prior[MONDAY]
    # for each prior[TUESDAY]
    # for each prior[WEDNESDAY]
    # for each prior[THURSDAY]
    # for each prior[FRIDAY]
    # for each prior[SATURDAY]
    # for each prior[SUNDAY]

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
