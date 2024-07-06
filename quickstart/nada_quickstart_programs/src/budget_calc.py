from nada_dsl import *

def nada_main():
    user = Party(name="User")

    # Define the secret inputs
    total_budget = SecretInteger(Input(name="total_budget", party=user))
    rent_expense = SecretInteger(Input(name="rent_expense", party=user))
    food_expense = SecretInteger(Input(name="food_expense", party=user))
    utilities_expense = SecretInteger(Input(name="utilities_expense", party=user))
    entertainment_expense = SecretInteger(Input(name="entertainment_expense", party=user))

    # Calculate total expenses
    total_expenses = rent_expense + food_expense + utilities_expense + entertainment_expense

    # Calculate remaining budget
    remaining_budget = total_budget - total_expenses

    # Return the output
    return [Output(remaining_budget, "remaining_budget", user)]