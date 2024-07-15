# Python `math` Module Assignment

## Task 1: Calculating Heights Using Trigonometry

1. **Scenario: Measuring a Flagpole**:
   - Imagine you're an engineer assessing the height of a flagpole.
   - Write a Python function called `calculate_height(angle_degrees, distance_meters)` that takes the angle of elevation (in degrees) and the distance from the flagpole (in meters).
   - Use trigonometry to calculate the height of the flagpole.
   - Display the result.

Example:
```python
import math

def calculate_height(angle_degrees, distance_meters):
    # Convert angle to radians
    angle_radians = math.radians(angle_degrees)
    
    # Calculate height using tangent function
    height = distance_meters * math.tan(angle_radians)
    
    return height

# Test case
flagpole_height = calculate_height(30, 10)
print(f"Flagpole height: {flagpole_height:.2f} meters")
```

## Task 2: Simulating Radioactive Decay

1. **Scenario: Radioactive Isotopes**:
   - Scientists study the decay of radioactive isotopes.
   - Write a Python function called `decay_amount(initial_amount, half_life_years, time_years)` that calculates the remaining amount of a radioactive substance.
   - Use the half-life concept: the time it takes for half of the substance to decay.
   - Display the remaining amount.

Example:
```python
def decay_amount(initial_amount, half_life_years, time_years):
    decay_constant = math.log(2) / half_life_years
    remaining_amount = initial_amount * math.exp(-decay_constant * time_years)
    return remaining_amount

# Test case
initial_amount = 1000  # Initial amount of a radioactive substance
half_life = 5          # Half-life in years
time_passed = 10       # Time passed in years
remaining = decay_amount(initial_amount, half_life, time_passed)
print(f"Remaining amount: {remaining:.2f}")
```

## Task 3: Calculating Combinations

1. **Scenario: Lottery Tickets**:
   - In a lottery, players choose a combination of numbers.
   - Write a Python function called `calculate_combinations(n, k)` that calculates the number of ways to choose `k` items from a set of `n` items (combinations).
   - Display the result.

Example:
```python
def calculate_combinations(n, k):
    combinations = math.comb(n, k)
    return combinations

# Test case
total_numbers = 49  # Total numbers in the lottery
chosen_numbers = 6  # Number of chosen lottery numbers
ways_to_win = calculate_combinations(total_numbers, chosen_numbers)
print(f"Ways to win: {ways_to_win}")
```