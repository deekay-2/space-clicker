import tkinter as tk
import random
import time

# A simple space‑themed reaction game.
# Humanized comments included so it feels like a real student project.

class SpaceClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 Space Clicker Game")

        # Game settings
        self.game_duration = 20   # how long the game lasts
        self.score = 0
        self.game_running = False
        self.start_time = None

        # Create a canvas with a space‑like background color
        self.canvas = tk.Canvas(root, width=500, height=350, bg="#0b0f29")
        self.canvas.pack()

        # Title / instructions
        self.info_label = tk.Label(root, text="Welcome to Space Clicker!",
                                   font=("Arial", 16), fg="white", bg="#0b0f29")
        self.canvas.create_window(250, 30, window=self.info_label)

        # Score + timer labels
        self.score_label = tk.Label(root, text="Score: 0",
                                    font=("Arial", 12), fg="white", bg="#0b0f29")
        self.canvas.create_window(80, 320, window=self.score_label)

        self.timer_label = tk.Label(root, text="Time: 20",
                                    font=("Arial", 12), fg="white", bg="#0b0f29")
        self.canvas.create_window(420, 320, window=self.timer_label)

        # Play button (starts in the center)
        self.play_button = tk.Button(root, text="PLAY", font=("Arial", 14, "bold"),
                                     bg="#4c8bf5", fg="white", width=10,
                                     command=self.start_game)
        self.canvas.create_window(250, 170, window=self.play_button)

        # The target button the player clicks
        self.target_button = tk.Button(root, text="⭐", font=("Arial", 18),
                                       bg="#f5d142", fg="black",
                                       command=self.on_target_click)

    def start_game(self):
        # Reset game state
        self.score = 0
        self.game_running = True
        self.start_time = time.time()

        self.score_label.config(text="Score: 0")
        self.info_label.config(text="Click the star as fast as you can!")

        # Hide the play button during the game
        self.play_button.place_forget()

        # Place the target in the center to start
        self.canvas.create_window(250, 170, window=self.target_button, tags="target")

        # Start the timer loop
        self.update_timer()

    def on_target_click(self):
        if not self.game_running:
            return

        # Increase score
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

        # Move the star to a random new location
        self.move_target_randomly()

    def move_target_randomly(self):
        self.canvas.delete("target")

        # Random position inside the canvas
        x = random.randint(40, 460)
        y = random.randint(60, 300)

        self.canvas.create_window(x, y, window=self.target_button, tags="target")

    def update_timer(self):
        if not self.game_running:
            return

        elapsed = time.time() - self.start_time
        time_left = int(self.game_duration - elapsed)

        if time_left <= 0:
            self.timer_label.config(text="Time: 0")
            self.end_game()
        else:
            self.timer_label.config(text=f"Time: {time_left}")
            self.root.after(200, self.update_timer)

    def end_game(self):
        self.game_running = False
        self.canvas.delete("target")

        self.info_label.config(text=f"Game Over! Final Score: {self.score}")

        # Bring back the play button so they can try again
        self.canvas.create_window(250, 170, window=self.play_button)


# Standard Tkinter startup
root = tk.Tk()
game = SpaceClicker(root)
root.mainloop()
