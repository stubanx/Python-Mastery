# Day 35

#### **Objective:**
This assignment is designed to help you understand and practice the concept of decorators in Python by applying them to solve real-life problems. You will create basic and advanced decorators, explore decorator chaining, and implement them in practical scenarios.

---

### **Part 1: Basic Decorator Practice**

**Task 1: Timing Decorator**

- **Problem Statement:** Create a decorator `timing_decorator` that calculates the time taken by a function to execute and prints the duration.
  
- **Requirements:**
  - Implement the decorator to time any function.
  - Use the decorator to time a function that calculates the factorial of a number.

- **Example Usage:**
  ```python
  @timing_decorator
  def calculate_factorial(n):
      result = 1
      for i in range(1, n + 1):
          result *= i
      return result

  print(calculate_factorial(10))
  ```

---

### **Part 2: Decorators with Arguments**

**Task 2: Authorization Decorator**

- **Problem Statement:** Create a decorator `require_role` that takes an argument `role` and checks if the user has the required role to execute a function. If not, raise an `AuthorizationError`.
  
- **Requirements:**
  - Implement the decorator to check for the required role.
  - Use the decorator to protect a function that should only be accessible by admins.

- **Example Usage:**
  ```python
  class AuthorizationError(Exception):
      pass

  @require_role("admin")
  def delete_database():
      print("Database deleted")

  user = {"username": "alice", "role": "admin"}
  delete_database(user)

  user = {"username": "bob", "role": "user"}
  # delete_database(user)  # Should raise AuthorizationError
  ```

---

### **Part 3: Advanced Decorators**

**Task 3: Retry Decorator**

- **Problem Statement:** Create a decorator `retry` that retries a function up to a specified number of times if it raises an exception. After exhausting all retries, the decorator should raise the original exception.
  
- **Requirements:**
  - Implement the decorator with a `retries` argument to specify the number of retries.
  - Use the decorator to simulate a network request that may fail intermittently.

- **Example Usage:**
  ```python
  import random

  @retry(retries=3)
  def unreliable_service():
      if random.choice([True, False]):
          raise ConnectionError("Failed to connect")
      return "Service response"

  print(unreliable_service())
  ```

---

### **Part 4: Real-Life Application of Decorators**

**Task 4: Caching Decorator (Memoization)**

- **Problem Statement:** Create a decorator `cache` that caches the results of a function to avoid redundant computations, especially for expensive operations like calculating Fibonacci numbers.
  
- **Requirements:**
  - Implement the decorator to cache function results.
  - Use the decorator to optimize the calculation of Fibonacci numbers.

- **Example Usage:**
  ```python
  @cache
  def fibonacci(n):
      if n in (0, 1):
          return n
      return fibonacci(n - 1) + fibonacci(n - 2)

  print(fibonacci(50))  # Should return quickly due to caching
  ```

---

### **Part 5: Decorator Chaining**

**Task 5: Chaining Decorators**

- **Problem Statement:** Create two decorators: 
  - `uppercase_decorator` that converts the result of a function to uppercase.
  - `exclamation_decorator` that adds "!!!" to the result of a function.
  
- **Requirements:**
  - Apply both decorators to a function that returns a greeting message.
  - Ensure the decorators are chained correctly.

- **Example Usage:**
  ```python
  @uppercase_decorator
  @exclamation_decorator
  def greet(name):
      return f"Hello, {name}"

  print(greet("Alice"))  # Should print "HELLO, ALICE!!!"
  ```

---

### **Part 6: Contextual Decorators**

**Task 6: Context-Aware Logging Decorator**

- **Problem Statement:** Create a decorator `contextual_logger` that logs the execution of a function along with contextual information like the user who triggered the function and the time of execution.
  
- **Requirements:**
  - Implement the decorator to include contextual logging.
  - Use the decorator to log access to a sensitive function.

- **Example Usage:**
  ```python
  @contextual_logger
  def access_sensitive_data(user, data_id):
      return f"Data {data_id} accessed by {user['username']}"

  user = {"username": "alice", "role": "admin"}
  print(access_sensitive_data(user, 42))
  ```

---

### **Part 7: Debugging and Testing**

**Task 7: Debugging Decorator**

- **Problem Statement:** Create a decorator `debug_decorator` that prints the function name, arguments, and return value each time a function is called. This is useful for debugging purposes.
  
- **Requirements:**
  - Implement the decorator to print debugging information.
  - Apply the decorator to a function that performs basic arithmetic operations.

- **Example Usage:**
  ```python
  @debug_decorator
  def add(a, b):
      return a + b

  print(add(5, 10))  # Should print debugging information
  ```

---
