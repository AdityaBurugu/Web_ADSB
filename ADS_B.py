from datetime import datetime

# Get the current time
current_time = datetime.now()

# Format the time as a string (optional)
formatted_time = current_time.strftime("%H:%M:%S")

print("Current Time:", formatted_time)
