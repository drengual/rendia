import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import subprocess
import random

def create_commit(commit_date, num_commits):
    date_str = commit_date.strftime("%a %b %d %H:%M:%S %Y +0000")
    for _ in range(num_commits):
        with open("activity.txt", "a") as f:
            f.write(f"Commit on {date_str}\n")
        subprocess.run(["git", "add", "activity.txt"])
        subprocess.run(["git", "commit", "-m", f"Work log {date_str}"])
        subprocess.run([
            "git", "commit", "--amend", "--no-edit",
            f"--date={date_str}"
        ])

def generate_commits(start_str, end_str):
    try:
        start_date = datetime.strptime(start_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_str, "%Y-%m-%d")
        delta = (end_date - start_date).days

        if delta <= 0:
            raise ValueError("End date must be after start date.")

        for day_offset in range(delta + 1):
            if random.random() < 0.3:  # 30% chance of committing on that day
                commit_date = start_date + timedelta(days=day_offset)
                num_commits = random.randint(1, 5)
                create_commit(commit_date, num_commits)

        messagebox.showinfo("Done", "Commits generated successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# UI part
root = tk.Tk()
root.title("Random Git Commit Generator")

tk.Label(root, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
start_entry = tk.Entry(root)
start_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="End Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
end_entry = tk.Entry(root)
end_entry.grid(row=1, column=1, padx=10, pady=5)

def on_generate():
    start_date = start_entry.get()
    end_date = end_entry.get()
    generate_commits(start_date, end_date)

generate_btn = tk.Button(root, text="Generate Commits", command=on_generate)
generate_btn.grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()
