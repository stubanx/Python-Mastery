# Day 38

#### **1. What is a Closure?**

A **closure** in Python is a function that captures the local variables from its enclosing scope when the function is defined and retains those variables even after the outer function has finished executing. This allows the inner function to access those captured variables later on.

In simpler terms, a closure is like a suitcase where the function packs variables before leaving a scope, and then carries this suitcase around even after the outer scope is gone.

---

### **2. Basic Concepts**

#### **2.1. Functions Inside Functions**

A closure typically involves:
- An **outer function** that defines a local variable.
- An **inner function** that is returned by the outer function and can access the local variable even after the outer function has completed.

**Example:**

```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
```

- **`outer_function(x)`** defines a variable `x` and returns `inner_function(y)`.
- **`inner_function(y)`** uses `x` from the outer scope.

**Usage:**

```python
closure = outer_function(10)
print(closure(5))  # Output: 15
```

Here, `closure` is a closure that remembers `x = 10` from the outer function, and later adds `5` to it.

#### **2.2. Why Use Closures?**

Closures are used for:
- **Encapsulation:** To create functions that have some private data.
- **Factory Functions:** To generate functions with pre-configured parameters.

---

### **3. Creating and Using Closures**

#### **3.1. Basic Closure Example**

Let’s create a simple closure that multiplies a number by a given factor.

**Example:**

```python
def multiplier(factor):
    def multiply_by(x):
        return x * factor
    return multiply_by
```

- **`multiplier(3)`** returns a function that multiplies by `3`.
- The returned function remembers the `factor` from the outer scope.

**Usage:**

```python
times_three = multiplier(3)
print(times_three(10))  # Output: 30
```

Here, `times_three` is a closure that multiplies any input by `3`.

#### **3.2. Closures with Mutable Objects**

Closures can also capture and retain mutable objects, such as lists.

**Example:**

```python
def make_counter():
    count = [0]  # List to retain state

    def counter():
        count[0] += 1
        return count[0]

    return counter
```

**Usage:**

```python
counter = make_counter()
print(counter())  # Output: 1
print(counter())  # Output: 2
print(counter())  # Output: 3
```

In this example, the list `count` retains its state across multiple calls to `counter()`.

---

### **4. Real-Life Applications of Closures**

#### **4.1. Function Factories**

Closures are often used to create functions dynamically, which can be very useful in scenarios where you need to generate multiple functions with different behaviors.

**Example: Discount Calculators**

```python
def discount_calculator(discount):
    def apply_discount(price):
        return price - (price * discount)
    return apply_discount
```

**Usage:**

```python
ten_percent_off = discount_calculator(0.10)
twenty_percent_off = discount_calculator(0.20)

print(ten_percent_off(100))  # Output: 90.0
print(twenty_percent_off(100))  # Output: 80.0
```

Here, `ten_percent_off` and `twenty_percent_off` are closures that apply different discounts.

#### **4.2. Logging with Closures**

Closures can also be used to create customized loggers that prefix log messages with specific tags.

**Example:**

```python
def logger(tag):
    def log_message(msg):
        print(f"[{tag}] {msg}")
    return log_message
```

**Usage:**

```python
error_logger = logger("ERROR")
info_logger = logger("INFO")

error_logger("This is an error message.")  # Output: [ERROR] This is an error message.
info_logger("This is an info message.")  # Output: [INFO] This is an info message.
```

Each logger retains its tag, making it easier to categorize log messages.

---

### **5. Advanced Concepts with Closures**

#### **5.1. Using Closures to Implement Decorators**

Decorators in Python are often implemented using closures. A decorator is a function that takes another function as an argument and extends or alters its behavior.

**Example: Timing a Function**

```python
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to complete")
        return result
    return wrapper
```

**Usage:**

```python
@time_decorator
def slow_function():
    time.sleep(2)
    return "Finished"

print(slow_function())
```

Here, the `time_decorator` is a closure that retains access to the original function `func` and its arguments.

#### **5.2. Managing State with Closures**

Closures can be used to manage state without the need for global variables or classes.

**Example: Accumulator**

```python
def accumulator(start):
    total = start

    def add(value):
        nonlocal total
        total += value
        return total

    return add
```

**Usage:**

```python
acc = accumulator(10)
print(acc(5))  # Output: 15
print(acc(10))  # Output: 25
```

In this example, `total` retains its state across multiple calls to the `add` function.

---

### **6. Extreme Use Cases**

#### **6.1. Closures for Caching**

You can use closures to implement simple caching mechanisms, which is useful for functions with expensive computations.

**Example: Fibonacci with Caching**

```python
def fibonacci():
    cache = {}

    def fib(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]

    return fib
```

**Usage:**

```python
fib = fibonacci()
print(fib(10))  # Output: 55
```

Here, the `cache` dictionary is retained in the closure, allowing the function to avoid recalculating Fibonacci numbers.

#### **6.2. Stateful Widgets in GUIs**

Closures can be used to manage the state of GUI widgets without the need for classes.

**Example: Button Click Counter**

```python
def button_click_counter():
    count = 0

    def on_click():
        nonlocal count
        count += 1
        print(f"Button clicked {count} times")

    return on_click
```

**Usage:**

```python
button_click = button_click_counter()
button_click()  # Output: Button clicked 1 times
button_click()  # Output: Button clicked 2 times
```

Each button retains its own click count, demonstrating how closures can manage state in a GUI context.

---

### **Conclusion**

Closures in Python are a powerful and flexible tool that allow you to retain and access the state of variables even after the outer function has completed. From simple applications like creating custom functions on the fly to more complex use cases like caching and state management, closures provide an elegant solution for a variety of programming challenges. Understanding and mastering closures will enhance your ability to write clean, efficient, and reusable code.