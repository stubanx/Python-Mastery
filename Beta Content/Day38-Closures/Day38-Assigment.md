### **Assignment: Mastering Python Closures through Real-Life Applications**

#### **Objective:**
This assignment will help you understand and practice the concept of closures in Python by applying them to solve real-world problems. You will explore how closures can retain state, manage encapsulated data, and create dynamic functions.

---

### **Part 1: Basic Closure Practice**

**Task 1: Personal Greeter**

- **Problem Statement:** Create a closure `personal_greeter` that generates a greeting message customized for a specific person.
  
- **Requirements:**
  - The outer function should accept a `name` argument.
  - The inner function should return a greeting that includes the `name`.
  
- **Example Usage:**
  ```python
  greet_john = personal_greeter("John")
  print(greet_john("Good morning"))  # Output: "Good morning, John!"
  ```

---

### **Part 2: Managing State with Closures**

**Task 2: Simple Counter**

- **Problem Statement:** Implement a closure `make_counter` that creates a counter function which increments and returns a count each time it is called.
  
- **Requirements:**
  - The outer function should initialize the count to zero.
  - The inner function should increment and return the current count.

- **Example Usage:**
  ```python
  counter = make_counter()
  print(counter())  # Output: 1
  print(counter())  # Output: 2
  print(counter())  # Output: 3
  ```

---

### **Part 3: Real-Life Applications of Closures**

**Task 3: Personalized Discount Calculator**

- **Problem Statement:** Create a closure `discount_calculator` that applies a specific discount rate to a product's price.
  
- **Requirements:**
  - The outer function should accept a `discount` rate.
  - The inner function should accept a `price` and return the discounted price.
  
- **Example Usage:**
  ```python
  ten_percent_off = discount_calculator(0.10)
  print(ten_percent_off(100))  # Output: 90.0
  ```

---

### **Part 4: Advanced Closure Practice**

**Task 4: Caching with Closures**

- **Problem Statement:** Implement a closure `cached_fibonacci` that caches the results of expensive Fibonacci calculations to improve performance.
  
- **Requirements:**
  - The outer function should initialize an empty cache.
  - The inner function should compute the Fibonacci number for a given input `n`, using the cache to store previously computed values.
  
- **Example Usage:**
  ```python
  fib = cached_fibonacci()
  print(fib(10))  # Output: 55
  print(fib(10))  # Should return the cached value without recomputation
  ```

---

### **Part 5: Real-World Contextual Applications**

**Task 5: Logger with Custom Tags**

- **Problem Statement:** Create a closure `tagged_logger` that generates a logger function with a custom tag for different types of log messages (e.g., `ERROR`, `INFO`).
  
- **Requirements:**
  - The outer function should accept a `tag`.
  - The inner function should accept a `message` and print it prefixed with the tag.
  
- **Example Usage:**
  ```python
  error_logger = tagged_logger("ERROR")
  info_logger = tagged_logger("INFO")
  
  error_logger("This is an error")  # Output: [ERROR] This is an error
  info_logger("This is information")  # Output: [INFO] This is information
  ```

---

### **Part 6: Exploring Complex Scenarios**

**Task 6: Stateful Button Click Counter**

- **Problem Statement:** Simulate a GUI button click counter using closures. Each button should have its own counter to track how many times it has been clicked.
  
- **Requirements:**
  - The outer function should return a click counter function.
  - The inner function should increment and return the number of clicks for that specific button.
  
- **Example Usage:**
  ```python
  button1_click = button_click_counter()
  button2_click = button_click_counter()
  
  print(button1_click())  # Output: 1
  print(button1_click())  # Output: 2
  print(button2_click())  # Output: 1
  ```

---

### **Part 7: Functional Programming with Closures**

**Task 7: Dynamic Function Generator**

- **Problem Statement:** Implement a closure `make_power_function` that generates a function to raise numbers to a specific power.
  
- **Requirements:**
  - The outer function should accept an exponent `n`.
  - The inner function should accept a base `x` and return `x` raised to the power of `n`.
  
- **Example Usage:**
  ```python
  square = make_power_function(2)
  cube = make_power_function(3)
  
  print(square(4))  # Output: 16
  print(cube(3))  # Output: 27
  ```

---
