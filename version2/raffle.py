"""Randomly pick customer and print customer info"""

# Import modules:
from random import choice
from customers import *

# raffle functions:
def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)
    
    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")


def run_raffle():
    """Run the weekly raffle from the terminal."""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)

run_raffle()