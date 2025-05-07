import random
from datetime import datetime

filename = "activity.txt"

num_updates = random.randint(3, 10)

with open(filename, "a") as f:
    for i in range(num_updates):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Update {i+1}/{num_updates} — {timestamp}\n")