# Day 24

1. **What Is the `math` Module?**
   - The `math` module is built into Python and provides mathematical functions and constants.
   - It's like a toolbox for number crunching, trigonometry, and more.

2. **Basic Functions**:
   - `math.ceil(x)`: Returns the smallest integer greater than or equal to `x`.
   - `math.floor(x)`: Returns the largest integer less than or equal to `x`.
   - `math.fabs(x)`: Returns the absolute value of `x`.
   - `math.factorial(n)`: Computes `n!` (n factorial).

3. **Advanced Functions**:
   - `math.comb(n, k)`: Calculates the binomial coefficient (ways to choose `k` items from `n` without repetition).
   - `math.copysign(x, y)`: Creates a float with the magnitude of `x` and the sign of `y`.
   - `math.fmod(x, y)`: Computes `x % y` (like the remainder, but with specific behavior).

4. **Real-Life Applications**:
   - **Statistics**: Calculate averages, standard deviations, and probabilities.
   - **Geometry**: Find areas, volumes, and angles.
   - **Financial Calculations**: Interest rates, compound growth, and amortization.
   - **Physics and Engineering**: Trajectories, waves, and forces.

5. **Example: Calculating Compound Interest**:
   ```python
   import math

   principal = 1000
   rate = 0.05
   time = 3

   # Compound interest formula
   compound_interest = principal * math.pow(1 + rate, time) - principal

   print(f"Compound interest after {time} years: ${compound_interest:.2f}")
   ```

the `math` module is your mathematical sidekick! 🧮🔍
