import tkinter as tk
from tkinter import messagebox


class AdventureGame:
    def __init__(self, master):  # Fixed the double underscores here
        self.master = master
        self.master.title("The Quest for the Lost Amulet")
        self.master.config(bg="#f0f0f0")  # Background color

        self.story_text = tk.StringVar()
        self.story_text.set("You find yourself in a small village surrounded by dense, dark woods. "
                            "The villagers speak of a lost amulet hidden deep within the forest. "
                            "What will you do?")

        self.label = tk.Label(master, textvariable=self.story_text, wraplength=300, bg="#f0f0f0", font=("Arial", 12))
        self.label.pack(pady=20)

        self.button_frame = tk.Frame(master, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        self.start_game()

    def start_game(self):
        self.clear_buttons()
        self.story_text.set("You stand at the edge of the village, where two paths diverge:")
        self.create_button("The Left Path: Into the heart of the forest", self.left_path, "#ff9999", "#ffcccc")
        self.create_button("The Right Path: To a winding river", self.right_path, "#99ccff", "#cce5ff")

    def left_path(self):
        self.clear_buttons()
        self.story_text.set(
            "You take the Left Path into the dark forest. After walking for a while, you hear a rustling sound.")
        self.create_button("Investigate the sound", self.investigate_sound, "#ffcc99", "#ffe6cc")
        self.create_button("Keep walking cautiously", self.keep_walking, "#99ff99", "#ccffe6")

    def right_path(self):
        self.clear_buttons()
        self.story_text.set("You take the Right Path to the river. At the riverbank, you see a shimmering creature.")
        self.create_button("Approach the creature", self.approach_creature, "#ffcc99", "#ffe6cc")
        self.create_button("Stay back and observe", self.observe_creature, "#99ff99", "#ccffe6")

    def investigate_sound(self):
        self.clear_buttons()
        self.story_text.set("You find a small fox caught in some vines.")
        self.create_button("Help the fox", self.help_fox, "#ff9999", "#ffcccc")
        self.create_button("Leave it and move on", self.leave_fox, "#99ccff", "#cce5ff")

    def keep_walking(self):
        self.clear_buttons()
        self.story_text.set("You walk cautiously but trip over a root and fall.")
        self.create_button("Try to get up", self.try_get_up, "#ff9999", "#ffcccc")
        self.create_button("Stay down and rest", self.stay_down, "#99ccff", "#cce5ff")

    def approach_creature(self):
        self.clear_buttons()
        self.story_text.set("The shimmering creature transforms into a wise spirit. It offers you a choice.")
        self.create_button("Choose knowledge", self.choose_knowledge, "#ffcc99", "#ffe6cc")
        self.create_button("Choose power", self.choose_power, "#99ff99", "#ccffe6")

    def observe_creature(self):
        self.clear_buttons()
        self.story_text.set("As you observe, the creature notices you and vanishes.")
        self.create_button("Search for it", self.search_creature, "#ffcc99", "#ffe6cc")
        self.create_button("Head back to the village", self.head_back, "#99ff99", "#ccffe6")

    def help_fox(self):
        messagebox.showinfo("You Win!", "The fox thanks you and leads you to the amulet!")
        self.master.quit()

    def leave_fox(self):
        messagebox.showinfo("Game Over", "You move on, but the forest grows darker. You lose your way.")
        self.master.quit()

    def try_get_up(self):
        messagebox.showinfo("Game Over", "You get up but find yourself surrounded by shadows.")
        self.master.quit()

    def stay_down(self):
        messagebox.showinfo("Game Over", "You rest for a while, but it's too quiet. You never wake up.")
        self.master.quit()

    def choose_knowledge(self):
        messagebox.showinfo("You Win!", "You gain wisdom and use it to help your village!")
        self.master.quit()

    def choose_power(self):
        messagebox.showinfo("Game Over", "You gain power but become a tyrant.")
        self.master.quit()

    def search_creature(self):
        messagebox.showinfo("You Win!", "You find the creature again, and it rewards you with the amulet!")
        self.master.quit()

    def head_back(self):
        messagebox.showinfo("Game Over", "You return to the village, but the adventure lingers in your heart.")
        self.master.quit()

    def create_button(self, text, command, bg_color, hover_color):
        button = tk.Button(self.button_frame, text=text, command=command, bg=bg_color, font=("Arial", 10), width=40)
        button.pack(pady=5)
        button.bind("<Enter>", lambda e: button.config(bg=hover_color))  # Change color on hover
        button.bind("<Leave>", lambda e: button.config(bg=bg_color))  # Revert color

    def clear_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()


if  __name__ == "__main__":  # Fixed the double underscores here
    root = tk.Tk()
    game = AdventureGame(root)
    root.mainloop()