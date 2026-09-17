from datetime import datetime, timedelta

# Get current time
now = datetime.now()
print("Current Time:", now)

# Format a date into a clean string (strftime)
clean_date = now.strftime("%Y-%m-%d %H:%M")
print("Formatted:", clean_date)

# Date arithmetic (Add 7 days)
future_date = now + timedelta(days=7)
print("Next Week:", future_date)
