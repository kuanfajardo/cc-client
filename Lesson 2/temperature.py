# Problem: Convert user-input celsius into fahrenheit

#-----------------------------------------+
#   Computational Thinking & Pseudocode   |
#-----------------------------------------+
"""
1. Get a temperature input in degrees celsius from the user.
2. Use our formula to calculate fahrenheit temperature.
3. Tell the user the temperature in degrees fahrenheit.

# Pseudocode:
celsius = input from user                   // 1
fahrenheit = (9/5) * celsius + 32           // 2
print fahrenheit to user                    // 3


More detailed:
1. Get a temperature input in degrees celsius from the user.
    1a. Get input from user
    1b. Evaluate input as number

2. Use our formula to calculate fahrenheit temperature.

3. Tell the user the temperature in degrees fahrenheit.


# Pseudocode:
raw_input = input from user                   // 1a
celsius = raw_input as decimal number         // 1b,
fahrenheit = (9/5) * celsius + 32             // 2
print fahrenheit to user                      // 3
"""

# Failed attempt!
# celsius = input("Enter a temperature in degrees celsius: ")

# raw_input = input from user
raw_input = input("Enter a temperature in degrees celsius: ")

# celsius = raw_input as decimal number
celsius = float(raw_input)

# fahrenheit = (9/5) * celsius + 32
fahrenheit = (9 / 5) * celsius + 32

# print fahrenheit to user
print("The temperature is", fahrenheit, "degrees fahrenheit.")
