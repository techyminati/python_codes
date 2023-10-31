import tkinter as tk
from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.is_running = False
        self.elapsed_time = timedelta(0)

        self.time_label = tk.Label(root, text="00:00.0", font=("Arial", 40))
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)

        self.time_label.pack()
        self.start_button.pack()
        self.stop_button.pack()
        self.reset_button.pack()

        self.update_time()

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = datetime.now() - self.elapsed_time
            self.update_time()

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.elapsed_time = datetime.now() - self.start_time

    def reset(self):
        self.is_running = False
        self.elapsed_time = timedelta(0)
        self.update_time()

    def update_time(self):
        if self.is_running:
            self.elapsed_time = datetime.now() - self.start_time
        time_str = str(self.elapsed_time).split('.')[0]
        self.time_label.config(text=time_str)
        self.root.after(100, self.update_time)

root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()
