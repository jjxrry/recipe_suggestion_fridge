# recipe list
recipes = [
    # Indian recipes
    ("Chicken Curry", "indian", ["chicken", "onion", "spices"]),
    ("Paneer Tikka", "indian", ["paneer", "yogurt", "spices"]),
    ("Chana Masala", "indian", ["chickpeas", "tomato", "onion", "spices"]),
    ("Lamb Vindaloo", "indian", ["lamb", "potato", "spices", "vinegar"]),
    ("Aloo Gobi", "indian", ["potato", "cauliflower", "spices"]),
    ("Dal Tadka", "indian", ["lentils", "onion", "garlic", "spices"]),
    ("Butter Chicken", "indian", ["chicken", "tomato", "butter", "spices"]),
    ("Jeera Rice", "indian", ["rice", "cumin", "butter"]),
    ("Baingan Bharta", "indian", ["eggplant", "tomato", "onion", "spices"]),
    ("Masoor Dal", "indian", ["red lentils", "tomato", "spices"]),
    ("Cabbage Sabzi", "indian", ["cabbage", "mustard seeds", "spices"]),
    ("Tamarind Rice", "indian", ["rice", "tamarind", "peanuts", "spices"]),
    ("Upma", "indian", ["semolina", "mustard seeds", "vegetables"]),
    ("Vegetable Pulao", "indian", ["rice", "mixed veggies", "spices"]),
    ("Rajma", "indian", ["kidney beans", "onion", "tomato", "spices"]),
    ("Palak Paneer", "indian", ["spinach", "paneer", "spices"]),
    ("Vegetable Korma", "indian", ["mixed veggies", "yogurt", "spices"]),
    ("Samosa", "indian", ["potato", "peas", "spices", "wrapper"]),
    ("Besan Chilla", "indian", ["gram flour", "onion", "spices"]),
    ("Methi Thepla", "indian", ["fenugreek", "flour", "spices"]),
    # Chinese recipes
    ("Sweet and Sour Pork", "chinese", ["pork", "pineapple", "peppers"]),
    ("Kung Pao Chicken", "chinese", ["chicken", "peanuts", "chili", "scallions"]),
    ("Mapo Tofu", "chinese", ["tofu", "ground pork", "chili bean paste", "scallions"]),
    ("Egg Fried Rice", "chinese", ["rice", "egg", "peas", "soy sauce"]),
    ("Spring Rolls", "chinese", ["cabbage", "carrot", "wrapper", "soy sauce"]),
    ("Lo Mein", "chinese", ["noodles", "soy sauce", "vegetables", "scallions"]),
    ("Wonton Soup", "chinese", ["wontons", "broth", "scallions"]),
    ("Char Siu", "chinese", ["pork", "hoisin", "honey", "soy sauce"]),
    ("Scallion Pancakes", "chinese", ["flour", "scallions", "oil", "salt"]),
    (
        "Chinese Eggplant Stir Fry",
        "chinese",
        ["eggplant", "soy sauce", "garlic", "chili"],
    ),
    ("Broccoli Beef", "chinese", ["beef", "broccoli", "soy sauce"]),
    ("Cabbage Stir Fry", "chinese", ["cabbage", "soy sauce", "garlic"]),
    ("Chicken Chow Mein", "chinese", ["noodles", "chicken", "cabbage", "carrot"]),
    ("Chinese Corn Soup", "chinese", ["corn", "egg", "broth", "scallions"]),
    ("Sesame Noodles", "chinese", ["noodles", "soy sauce", "sesame oil", "scallions"]),
    ("Hot and Sour Soup", "chinese", ["tofu", "vinegar", "mushroom", "chili"]),
    (
        "Dan Dan Noodles",
        "chinese",
        ["noodles", "ground pork", "chili oil", "scallions"],
    ),
    ("Moo Shu Pork", "chinese", ["pork", "cabbage", "pancake", "hoisin"]),
    ("General Tso’s Chicken", "chinese", ["chicken", "soy sauce", "sugar", "chili"]),
    ("Egg Drop Soup", "chinese", ["egg", "broth", "cornstarch", "scallions"]),
    # Japanese recipes
    ("Sushi", "japanese", ["rice", "fish", "seaweed"]),
    ("Ramen", "japanese", ["noodles", "pork", "egg", "scallions"]),
    ("Tempura", "japanese", ["shrimp", "vegetables", "tempura batter"]),
    ("Onigiri", "japanese", ["rice", "seaweed", "filling"]),
    ("Miso Soup", "japanese", ["miso paste", "tofu", "scallions", "broth"]),
    ("Tamago Sushi", "japanese", ["egg", "rice", "seaweed"]),
    ("Chicken Teriyaki", "japanese", ["chicken", "soy sauce", "sugar", "mirin"]),
    ("Udon Noodles", "japanese", ["udon", "broth", "scallions"]),
    ("Yakitori", "japanese", ["chicken", "soy sauce", "sugar", "skewers"]),
    ("Cucumber Sunomono", "japanese", ["cucumber", "vinegar", "sugar", "salt"]),
    ("Tonkatsu", "japanese", ["pork cutlet", "egg", "panko", "oil"]),
    ("Japanese Curry Rice", "japanese", ["curry roux", "rice", "potato", "carrot"]),
    ("Zaru Soba", "japanese", ["soba noodles", "dipping sauce", "scallions"]),
    ("Oyakodon", "japanese", ["chicken", "egg", "onion", "rice"]),
    ("Mochi", "japanese", ["rice flour", "sugar", "water"]),
    ("Okonomiyaki", "japanese", ["flour", "cabbage", "egg", "sauce"]),
    ("Takoyaki", "japanese", ["octopus", "batter", "scallions", "sauce"]),
    ("Gyudon", "japanese", ["beef", "onion", "rice", "soy sauce"]),
    ("Katsu Don", "japanese", ["pork cutlet", "egg", "onion", "rice"]),
    ("Chawanmushi", "japanese", ["egg", "broth", "mushroom", "chicken"]),
]


# fridge only contains ingredients
# Fridge One:
# - Indian: "chicken", "onion", "spices" (for Chicken Curry)
# - Chinese: "pork", "pineapple", "peppers" (for Sweet and Sour Pork)
# - Chinese: "rice", "egg", "peas", "soy sauce" (for Egg Fried Rice)
# - Chinese: "cabbage", "soy sauce", "garlic" (for Cabbage Stir Fry)
# - Chinese: "egg", "broth", "cornstarch", "scallions" (for Egg Drop Soup)
# - Japanese: "rice", "fish", "seaweed" (for Sushi)
# - Japanese: "egg", "rice", "seaweed" (for Tamago Sushi)
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
    ("soy sauce", "condiment", 2),
    ("ginger", "spice", 1),
    ("garlic", "vegetable", 3),
    ("carrot", "vegetable", 2),
    ("miso paste", "condiment", 1),
    ("egg", "dairy", 3),
    ("peas", "vegetable", 2),
    ("cabbage", "vegetable", 2),
    ("salt", "seasoning", 1),
    ("sugar", "sweetener", 1),
    ("butter", "dairy", 2),
    ("napkin", "non-food", 10),
    ("soda", "beverage", 2),
    ("candle", "non-food", 1),
]


# Fridge Two:
# - Indian: "chickpeas", "tomato", "onion", "spices" (for Chana Masala)
# - Chinese: "chicken", "peanuts", "chili", "scallions" (for Kung Pao Chicken)
# - Chinese: "tofu", "ground pork", "chili bean paste", "scallions" (for Mapo Tofu)
# - Chinese: "rice", "egg", "peas", "soy sauce" (for Egg Fried Rice)
# - Chinese: "cabbage", "carrot", "wrapper", "soy sauce" (for Spring Rolls)
# - Chinese: "noodles", "soy sauce", "vegetables", "scallions" (for Lo Mein)
# - Japanese: "noodles", "pork", "egg", "scallions" (for Ramen)
# - Chinese: "cabbage", "soy sauce", "garlic" (for Cabbage Stir Fry)
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
    ("garlic", "vegetable", 3),
    ("bok choy", "vegetable", 2),
    ("soy sauce", "condiment", 2),
    ("tofu", "soy", 2),
    ("ginger", "spice", 2),
    ("mustard seeds", "spice", 1),
    ("cabbage", "vegetable", 2),
    ("carrot", "vegetable", 2),
    ("wrapper", "baking", 2),
    ("peas", "vegetable", 2),
    ("bubble wrap", "non-food", 1),
]


# Fridge Three:
# - Indian: "paneer", "yogurt", "spices" (for Paneer Tikka)
# - Chinese: "tofu", "ground pork", "chili bean paste", "scallions" (for Mapo Tofu)
# - Chinese: "flour", "scallions", "oil", "salt" (for Scallion Pancakes)
# - Japanese: "shrimp", "vegetables", "tempura batter" (for Tempura)
# - Japanese: "egg", "rice", "seaweed" (for Tamago Sushi)
# - Japanese: "cucumber", "vinegar", "sugar", "salt" (for Cucumber Sunomono)
# - Japanese: "chicken", "egg", "onion", "rice" (for Oyakodon)
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
    ("rice", "grain", 3),
    ("ginger", "spice", 2),
    ("soy sauce", "condiment", 2),
    ("flour", "baking", 2),
    ("mushrooms", "vegetable", 2),
    ("egg", "dairy", 3),
    ("seaweed", "vegetable", 2),
    ("sugar", "sweetener", 2),
    ("cucumber", "vegetable", 2),
    ("vinegar", "condiment", 1),
    ("mug", "non-food", 1),
    ("grape jelly", "spread", 1),
]
