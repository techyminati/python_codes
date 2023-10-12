import random

def roll_dice(num_dice=1, num_sides=6):
    if num_dice < 1 or num_sides < 2:
        return "Invalid input. Please provide valid values for the number of dice and sides."

    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls

def main():
    print("Welcome to the Dice Rolling Game!")

    while True:
        num_dice = int(input("Enter the number of dice to roll: "))
        num_sides = int(input("Enter the number of sides on each die: "))

        rolls = roll_dice(num_dice, num_sides)

        print("\nRoll result:")
        if num_dice == 1:
            print(f"You rolled a {rolls[0]}!")
        else:
            print(f"You rolled: {', '.join(map(str, rolls))} (Total: {sum(rolls)})")

        play_again = input("\nRoll the dice again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
