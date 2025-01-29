from datetime import datetime

# Get current date and time
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to version.md
with open("version.md", "w") as file:
    file.write(now + "\n")
