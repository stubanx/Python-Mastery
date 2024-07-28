

# Python `random` Module Assignment

## Task 1: Simulating Dice Rolls

1. **Scenario: Rolling a Six-Sided Die**:
   - Imagine you're building a board game.
   - Write a Python function called `roll_dice()` that simulates rolling a six-sided die.
   - Use the `random.randint(a, b)` function to generate a random integer between 1 and 6 (inclusive).
   - Display the result.

Example:
```python
import random

def roll_dice():
    return random.randint(1, 6)

# Test case
print("Rolled:", roll_dice())  # Output: A random integer between 1 and 6
```

## Task 2: Generating Random Passwords

1. **Scenario: User Registration**:
   - When users sign up for your website, you need to generate secure passwords.
   - Write a Python function called `generate_password(length)` that generates a random password of the specified length.
   - Use a combination of uppercase letters, lowercase letters, digits, and special characters.
   - Display the generated password.

Example:
```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

# Test case
print("Generated password:", generate_password(10))
```

## Task 3: Random Sampling

1. **Scenario: Survey Data Analysis**:
   - You have survey responses from a large group of people.
   - Write a Python function called `select_random_sample(data, sample_size)` that selects a random sample from the dataset.
   - Use `random.sample(data, sample_size)` to avoid repetition.
   - Display the sample.

Example:
```python
def select_random_sample(data, sample_size):
    sample = random.sample(data, sample_size)
    return sample

# Test case (replace with your own dataset)
survey_responses = ["Excellent", "Good", "Average", "Poor", "Very Poor"]
sample_result = select_random_sample(survey_responses, 3)
print("Random sample:", sample_result)
```

