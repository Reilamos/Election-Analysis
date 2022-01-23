# Create a variable called 'name' that holds a string
name = "Zon"

# Create a variable called 'country' that holds a string
country = "Mos Eisle"

# Create a variable called 'age' that holds an integer

age = 157

# Create a variable called 'hourly_wage' that holds an integer

hourly_earnings = 800

# Calculate the daily wage for the user

daily_earnings = hourly_earnings * 8
# Create a variable called 'satisfied' that holds a boolean
satisfied = True

# Print out "Hello <name>!"
print("hello " + name + "!")

# Print out what country the user entered

print("You live in", country)
# Print out the user's age
print("You are ", str(age) + "tears old")

# With an f-string, print out the daily wage that was calculated
print(f"Calculated daily wage is {daily_earnings}")

# With an f-string, print out whether the users were satisfied

print(f"You are satisfied with your daily wage? I'd say {satisfied}")