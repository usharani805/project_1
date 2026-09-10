from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()

print("Current Date and Time:", now)

# Display date separately
print("Date:", now.strftime("%Y-%m-%d"))

# Display time separately
print("Time:", now.strftime("%H:%M:%S"))

# Add 7 days to the current date
future_date = now + timedelta(days=7)

print("Date after 7 days:", future_date.strftime("%Y-%m-%d"))

# Calculate the difference between two dates
date1 = datetime(2026, 8, 26)
date2 = datetime(2026, 9, 5)

difference = date2 - date1

print("Difference between dates:", difference.days, "days")