### **Assignment: Mastering Python Iterators through Real-Life Application-Based Problems**

#### **Objective:**
The goal of this assignment is to help you understand the concept of iterators in Python by applying them to real-life scenarios. You will create your own iterators, work with generator functions, and use advanced iteration techniques to solve practical problems.

---

### **Part 1: Creating Custom Iterators**

**Task 1: Days of the Week Iterator**

- **Problem Statement:** Create a custom iterator class `DaysOfWeek` that returns the days of the week, starting from Monday. Once it reaches Sunday, it should raise a `StopIteration`.
  
- **Requirements:**
  - Implement the `__iter__()` and `__next__()` methods.
  - The iterator should return one day at a time when used in a loop.

- **Example Output:**
  ```python
  days = DaysOfWeek()
  for day in days:
      print(day)
  
  # Output:
  # Monday
  # Tuesday
  # Wednesday
  # Thursday
  # Friday
  # Saturday
  # Sunday
  ```

**Task 2: Countdown Iterator**

- **Problem Statement:** Create an iterator class `Countdown` that takes an integer `n` and counts down from `n` to 1. Once it reaches 1, it should raise a `StopIteration`.
  
- **Requirements:**
  - Implement the `__iter__()` and `__next__()` methods.
  - The iterator should work for any positive integer.

- **Example Output:**
  ```python
  countdown = Countdown(5)
  for number in countdown:
      print(number)
  
  # Output:
  # 5
  # 4
  # 3
  # 2
  # 1
  ```

---

### **Part 2: Working with Generator Functions**

**Task 3: Prime Number Generator**

- **Problem Statement:** Write a generator function `generate_primes` that yields prime numbers indefinitely, starting from 2. Use this generator to print the first 10 prime numbers.
  
- **Requirements:**
  - Implement the generator using the `yield` keyword.
  - Create a loop that breaks after receiving the first 10 primes.

- **Example Output:**
  ```python
  primes = generate_primes()
  for _ in range(10):
      print(next(primes))
  
  # Output:
  # 2
  # 3
  # 5
  # 7
  # 11
  # 13
  # 17
  # 19
  # 23
  # 29
  ```

**Task 4: Fibonacci Sequence Generator**

- **Problem Statement:** Write a generator function `fibonacci_sequence` that yields the Fibonacci sequence indefinitely. Print the first 15 Fibonacci numbers using this generator.
  
- **Requirements:**
  - Implement the generator using the `yield` keyword.
  - Create a loop that prints the first 15 numbers from the generator.

- **Example Output:**
  ```python
  fibonacci = fibonacci_sequence()
  for _ in range(15):
      print(next(fibonacci))
  
  # Output:
  # 0
  # 1
  # 1
  # 2
  # 3
  # 5
  # 8
  # 13
  # 21
  # 34
  # 55
  # 89
  # 144
  # 233
  # 377
  ```

---

### **Part 3: Real-Life Application of Iterators**

**Task 5: Streaming Stock Prices**

- **Problem Statement:** Imagine you have a continuous stream of stock prices coming in. Create a generator function `stream_stock_prices` that yields random stock prices (between $50 and $150) indefinitely. Simulate this by printing the first 20 prices with a 0.5-second delay between each price.

- **Requirements:**
  - Use the `yield` keyword to create the generator.
  - Use the `time.sleep(0.5)` function to simulate the delay.
  - Print the first 20 stock prices.

- **Example Output:**
  ```python
  import random
  import time
  
  stock_prices = stream_stock_prices()
  for _ in range(20):
      print(f"Stock Price: ${next(stock_prices):.2f}")
  
  # Output (Example):
  # Stock Price: $120.34
  # Stock Price: $78.56
  # Stock Price: $140.78
  # ...
  ```

**Task 6: Processing Large Log Files**

- **Problem Statement:** You have a large log file where each line is a log entry. Create an iterator `LogFileIterator` that reads the log file line by line and processes each line. Simulate processing by printing the first 10 lines from the log file.

- **Requirements:**
  - Implement the `__iter__()` and `__next__()` methods.
  - Ensure that the file is closed after reading all lines.
  - Create a small text file `log.txt` with at least 15 lines of dummy log data to test your iterator.

- **Example Output:**
  ```python
  logs = LogFileIterator('log.txt')
  for i, log in enumerate(logs):
      if i == 10:  # Limit to the first 10 logs
          break
      print(log)
  
  # Output:
  # 2024-08-12 10:00:01: User logged in
  # 2024-08-12 10:00:02: User viewed page
  # ...
  ```

---

### **Part 4: Advanced Iteration with `itertools`**

**Task 7: Round Robin Scheduler**

- **Problem Statement:** Use the `itertools.cycle` function to create a round-robin scheduler that iterates over a list of tasks indefinitely. Simulate a scenario where there are three tasks, and each task should be performed in a round-robin manner 5 times.

- **Requirements:**
  - Use `itertools.cycle` to create the round-robin iterator.
  - Print out the task name in each iteration.

- **Example Output:**
  ```python
  tasks = ["Task A", "Task B", "Task C"]
  round_robin = itertools.cycle(tasks)
  
  for _ in range(15):  # 5 times for each task
      print(next(round_robin))
  
  # Output:
  # Task A
  # Task B
  # Task C
  # Task A
  # Task B
  # Task C
  # ...
  ```

**Task 8: Generating Permutations of a Word**

- **Problem Statement:** Write a program that uses `itertools.permutations` to generate and print all the possible permutations of the letters in the word "ABC".

- **Requirements:**
  - Use `itertools.permutations` to generate the permutations.
  - Print each permutation on a new line.

- **Example Output:**
  ```python
  permutations = itertools.permutations('ABC')
  for perm in permutations:
      print(''.join(perm))
  
  # Output:
  # ABC
  # ACB
  # BAC
  # BCA
  # CAB
  # CBA
  ```

---

### **Submission Guidelines:**

- Submit your Python scripts for each task.
- Ensure your code is well-documented with comments explaining the logic.
- Include a brief explanation of what you learned from each task.

**Deadline:** [Specify Deadline]

---

This assignment is designed to deepen your understanding of Python iterators and how they can be applied in real-world scenarios. Happy coding!