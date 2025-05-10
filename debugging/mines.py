#!/usr/bin/python3
import random, os, sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, num_mines=10):
        self.width  = width
        self.height = height
        # place mines as flat indices
        self.mines = set(random.sample(range(width * height), num_mines))
        self.revealed = [[False]*width for _ in range(height)]

    # … count_mines_nearby and reveal() unchanged …

    def play(self):
        safe_count = self.width * self.height - len(self.mines)
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                # ═══ FIX #1: bounds check ═══
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of range! Try again.")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("💥 Game Over! You hit a mine.")
                    break

                # ═══ FIX #2: win detection ═══
                revealed = sum(sum(row) for row in self.revealed)
                if revealed == safe_count:
                    self.print_board(reveal=True)
                    print("🏆 You’ve cleared all safe squares!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

