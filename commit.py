import os
import random
import datetime
import subprocess
import json
import pytz

quotes = [
    "Progress, not perfection.",
    "Small steps every day.",
    "Consistency is more important than intensity.",
    "Keep moving forward.",
    "One step at a time.",
    "Stay consistent.",
    "Daily improvement.",
    "Building habits.",
    "Steady progress.",
    "Keep going."
]

commit_messages = [
    "Update project files",
    "Minor improvements",
    "Code cleanup",
    "Routine maintenance",
    "Update documentation",
    "Small progress update",
    "Sync latest changes",
    "General improvements",
    "File organization",
    "Daily progress commit",
    "Maintain project structure",
    "Incremental update"
]

target_files = ["daily_log.txt", "progress.md", "inspiration.txt"]

ist = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(ist)
date_key = now.strftime('%Y-%m-%d')
timestamp = now.strftime('%Y-%m-%d %I:%M:%S %p')

counter_file = ".commit_tracker.json"
max_total = 12

if os.path.exists(counter_file):
    with open(counter_file, "r") as f:
        data = json.load(f)
else:
    data = {}

done = data.get(date_key, 0)
remaining = max_total - done

if remaining <= 0:
    print("Max commits reached for today.")
    exit(0)

slot_commit = random.randint(2, 5)
slot_commit = min(slot_commit, remaining)

for _ in range(slot_commit):
    quote = random.choice(quotes)
    message = random.choice(commit_messages)
    filename = random.choice(target_files)

    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {quote}\n")

    subprocess.run(["git", "add", filename], check=False)
    subprocess.run(["git", "commit", "-m", message], check=False)

data[date_key] = done + slot_commit
with open(counter_file, "w") as f:
    json.dump(data, f)

print(f"{slot_commit} commit(s) made at {timestamp}. Total today: {done + slot_commit}")
