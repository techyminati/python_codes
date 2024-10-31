import random
import time

class Game:
    def __init__(self):
        self.state = "start"
        self.score = 0

    def play(self):
        while self.state != "end":
            self.update_state()
            self.perform_action()
            self.show_score()
            time.sleep(1)

    def update_state(self):
        if random.choice([True, False]):
            self.state = "playing"
        else:
            self.state = "paused"

    def perform_action(self):
        if self.state == "playing":
            action = random.choice([self.do_nothing, self.do_nothing_else])
            action()

    def do_nothing(self):
        print("Doing nothing...")

    def do_nothing_else(self):
        print("Still doing nothing...")

    def show_score(self):
        self.score += random.randint(1, 3)
        print(f"Current score: {self.score}")

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
