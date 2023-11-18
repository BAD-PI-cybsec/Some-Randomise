import random 
import time

# Initialize the remaining gold
remaining_gold = 1000

# Define the winning number
winning_number = random.randint(0, 30)

# Play the game until the user runs out of gold
while remaining_gold > 0:
    # Ask the user how much gold they want to bet
    gold_input = ''
    while not gold_input.isdigit() or int(gold_input) > remaining_gold or int(gold_input) < 1:
        gold_input = input(f"How much gold would you like to bet? (1-{remaining_gold}): ")

    chosen_gold = int(gold_input)

    # Ask the user to choose a number
    number_input = ''
    while not number_input.isdigit() or int(number_input) < 0 or int(number_input) > 30:
        number_input = input("Choose a number between 0-30: ")

    chosen_number = int(number_input)

    # Generate a random number from 0 to 30
    spinner = []
    for i in range(20):
        n = random.randint(0, 30)
        spinner.append(n)
        print("The numbers are spinning... ", spinner)
        time.sleep(0.05)
    random_number = spinner[-1]

    # Check if the user guessed correctly
    if chosen_number == random_number:
        if random_number == winning_number:
            if winning_number == 0:
                chosen_gold *= 5
            elif winning_number % 2 == 1:
                chosen_gold *= 1.5
            print(f"Congratulations, {chosen_number} was correct! You won {chosen_gold} gold!")
        else:
            print("Sorry, you guessed the wrong winning number.")
    else:
        print(f"Sorry, your guess of {chosen_number} did not match the winning number of {winning_number}.")

    # Update the remaining gold
    remaining_gold -= chosen_gold

    # End the game if the user runs out of gold
    if remaining_gold == 0:
        print("You have run out of gold. Game over.")
        break

    # Ask the user if they want to play again
    play_again = input("Would you like to keep playing? (y/n): ")
    if play_again.lower() == 'n':
        print("Thanks for playing!")
        break
    elif play_again.lower() == 'y':
        print(f"Remaining gold: {remaining_gold}")
        winning_number = random.randint(0, 30)
    else:
        print("Invalid input. Game over.")
        break
