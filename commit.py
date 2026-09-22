import os
import random
import datetime
import subprocess
import json
import pytz

quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Success is the sum of small efforts, repeated.",
    "Small steps every day.",
    "One more brick in the wall of progress.",
    "Consistency is more important than intensity.",
    "Another line, another win!",
    "Stay curious, keep learning.",
    "Another commit to greatness.",
    "Progress, not perfection.",
    "Just showing up matters.",
    "Every commit counts toward greatness.",
    "Build something you're proud of.",
    "Bit by bit, you create the masterpiece.",
    "The habit of showing up wins the game.",
    "Don’t break the streak — commit today!",
    "From bugs to brilliance — keep coding!",
    "It’s not about perfection. It’s about progress.",
    "You’re one step closer to your goal.",
    "Keep calm and commit on.",
    "Even a tiny push moves the needle."
]

commit_messages = [
    "Update project files",
    "Minor improvements",
    "Code cleanup",
    "Refactor small sections",
    "Improve documentation",
    "Fix formatting issues",
    "Update daily notes",
    "Small progress update",
    "Maintain project structure",
    "Routine maintenance",
    "Sync latest changes",
    "Adjust configuration",
    "Update tracking files",
    "General improvements",
    "Clean up repository",
    "Incremental update",
    "Project maintenance",
    "File organization",
    "Content update",
    "Daily progress commit"
]

target_files = ["daily_log.txt", "progress.md", "inspiration.txt"]

ist = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(ist)
date_key = now.strftime('%Y-%m-%d')
timestamp = now.strftime('%Y-%m-%d %I:%M:%S %p')

counter_file = ".commit_tracker.json"
min_total = 3
max_total = 12

if os.path.exists(counter_file):
    with open(counter_file, "r") as f:
        data = json.load(f)
else:
    data = {}

# Daily count
done = data.get(date_key, 0)
remaining = max_total - done

if remaining <= 0:
    print("Max commits reached for today.")
    exit()

# Make 1 to 4 commits each run
slot_commit = random.randint(1, 4)
slot_commit = min(slot_commit, remaining)

# Make sure we reach at least min_total
if done + slot_commit < min_total:
    slot_commit = min(min_total - done, remaining)

log_entries = []

for _ in range(slot_commit):
    quote = random.choice(quotes)
    message = random.choice(commit_messages)
    filename = random.choice(target_files)

    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {quote}\n")

    subprocess.run(["git", "add", filename], check=False)
    subprocess.run(["git", "commit", "-m", message], check=False)
    log_entries.append(f"[{timestamp}] - {message}")

# Update tracking
data[date_key] = done + slot_commit
with open(counter_file, "w") as f:
    json.dump(data, f)

if slot_commit > 0:
    with open("commit_log.txt", "a") as log:
        log.write(f"[{timestamp}] +{slot_commit} commit(s)\n")
        log.write("\n".join(log_entries) + "\n\n")

print(f"{slot_commit} commit(s) made at {timestamp}. Total today: {done + slot_commit}")
