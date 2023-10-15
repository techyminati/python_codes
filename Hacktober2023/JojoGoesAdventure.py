import time

# Define the player
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount

# Define game scenes
def start_game():
    print("Welcome to the Adventure, Jojo!")
    print("You find yourself in a mysterious forest.")

def explore_forest(player):
    print("You venture deeper into the forest.")
    print("Suddenly, you encounter a wild animal!")
    choice = input("Do you 'fight' or 'run' away? ").lower()

    if choice == "fight":
        print("You engage in a battle but get wounded.")
        player.take_damage(20)
        print("You managed to defeat the animal but lost some health.")
    elif choice == "run":
        print("You decide to run away and find a safe spot to rest.")
        player.heal(10)
        print("You've healed a bit and your health is now", player.health)

def end_game(player):
    print("The adventure comes to an end.")
    if player.is_alive():
        print("Congratulations, Jojo! You survived the adventure with", player.health, "health remaining.")
    else:
        print("Unfortunately, Jojo didn't make it. Better luck next time!")

# Main game loop
def adventure_game():
    player_name = "Jojo"
    jojo = Player(player_name)
    start_game()

    while jojo.is_alive():
        explore_forest(jojo)

    end_game(jojo)

# Start the adventure game
adventure_game()
