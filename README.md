🔍 Goal: Recommend recipes based on available ingredients in the fridge

🤖 AI Model: Naive Bayes classifier (ingredients → recipe prediction)

📥 Input: User inputs whether

📤 Output: Top recipe suggestions ranked by user preference, calculated based on user Priors that are already given.

🔁 Personalization: Learns from user feedback (likes/dislikes)

🌟 Unique Angle: Lightweight, personalized, fridge-friendly AI that adapts over time

Ingredients Ex.
{ID: 1 (eggs), Shelf life, Does user Like it (0 - 1)}
{recipe ID, difficulty level, efficacy level}

We have built a program to iteratively update the priors based on user feedback from using bayesian sampling. We have built a program to present the prior based probabilities to the user, to recommend any fitting recipe for the given day based on what is in their fridge. We can then take their probabilites and update each prior for the next week given a user rating on the recommended recipe (0.0 - 1.0). 

To work the program, the user should:

- Setup Venv

- Install requirements.txt

- Run 8_days_simulation.py (python3 8_days_simulation.py)

- Pick recommended recipe per day, rate the recipes for the week, see the model update the priors for the next week.
