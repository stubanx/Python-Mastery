
#### **Objective:**
This assignment will help you understand and practice the concept of generators in Python by applying them to solve real-world problems. You will create basic and advanced generators, explore their use in memory-efficient processing, and implement them in practical scenarios.

---

### **Part 1: Basic Generator Practice**

**Task 1: Number Series Generator**

- **Problem Statement:** Create a generator `number_series` that generates a sequence of numbers starting from a given number, incrementing by a specified step.
  
- **Requirements:**
  - The generator should accept two arguments: `start` (the starting number) and `step` (the increment).
  - The generator should yield the numbers in the sequence indefinitely.

- **Example Usage:**
  ```python
  gen = number_series(10, 2)
  for _ in range(5):
      print(next(gen))  # Output: 10, 12, 14, 16, 18
  ```

---

### **Part 2: Real-Life Applications of Generators**

**Task 2: Log File Reader**

- **Problem Statement:** Create a generator `log_reader` that reads a large log file line by line, processing each line on the fly without loading the entire file into memory.
  
- **Requirements:**
  - The generator should accept a file path as an argument.
  - Use the generator to process and print the first 10 lines of a large log file.

- **Example Usage:**
  ```python
  for line in log_reader('server_logs.txt'):
      print(line.strip())
  ```

---

### **Part 3: Infinite Generators**

**Task 3: Infinite Fibonacci Generator**

- **Problem Statement:** Create a generator `infinite_fibonacci` that generates the Fibonacci sequence indefinitely.
  
- **Requirements:**
  - The generator should yield each Fibonacci number in the sequence, starting from 0.
  - Use the generator to print the first 10 Fibonacci numbers.

- **Example Usage:**
  ```python
  fib_gen = infinite_fibonacci()
  for _ in range(10):
      print(next(fib_gen))  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
  ```

---

### **Part 4: Generator Expressions**

**Task 4: Squares Generator Expression**

- **Problem Statement:** Use a generator expression to create a sequence of squares of numbers from 1 to 100. Then, sum up all the squares using the generator expression.
  
- **Requirements:**
  - The generator expression should produce squares of numbers from 1 to 100.
  - Calculate the sum of these squares without storing them in a list.

- **Example Usage:**
  ```python
  squares_gen = (x * x for x in range(1, 101))
  total = sum(squares_gen)
  print(total)  # Output: 338350
  ```

---

### **Part 5: Advanced Generator Practice**

**Task 5: Prime Number Generator**

- **Problem Statement:** Create a generator `prime_generator` that generates prime numbers indefinitely.
  
- **Requirements:**
  - The generator should yield each prime number in the sequence, starting from 2.
  - Use the generator to print the first 10 prime numbers.

- **Example Usage:**
  ```python
  prime_gen = prime_generator()
  for _ in range(10):
      print(next(prime_gen))  # Output: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
  ```

---

### **Part 6: Generators with `yield from`**

**Task 6: Nested Generators**

- **Problem Statement:** Create two generators, `sub_generator` and `main_generator`. The `sub_generator` should yield a series of numbers, and the `main_generator` should use `yield from` to delegate to `sub_generator` and then continue yielding its own values.
  
- **Requirements:**
  - Implement `sub_generator` to yield the numbers 1, 2, and 3.
  - Implement `main_generator` to yield values from `sub_generator` and then yield 4, 5, and 6.

- **Example Usage:**
  ```python
  def sub_generator():
      yield 1
      yield 2
      yield 3

  def main_generator():
      yield from sub_generator()
      yield 4
      yield 5
      yield 6

  for value in main_generator():
      print(value)  # Output: 1, 2, 3, 4, 5, 6
  ```

---

### **Part 7: Contextual and Complex Applications**

**Task 7: Stream Data Processing**

- **Problem Statement:** Simulate a data stream that yields sensor readings from multiple sensors. Each sensor generates a reading every second. Use a generator to handle this simulation efficiently.
  
- **Requirements:**
  - Create a generator `sensor_data_stream` that yields simulated sensor readings as `(sensor_id, value)` tuples.
  - Simulate readings from 3 sensors over 5 seconds and print each reading.

- **Example Usage:**
  ```python
  import random
  import time

  def sensor_data_stream(num_sensors):
      while True:
          for sensor_id in range(1, num_sensors + 1):
              yield (sensor_id, random.uniform(20.0, 25.0))
          time.sleep(1)

  stream = sensor_data_stream(3)
  for _ in range(15):  # 5 seconds, 3 sensors per second
      print(next(stream))
  ```

---
