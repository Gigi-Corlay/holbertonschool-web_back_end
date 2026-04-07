# holbertonschool-web_back_end

## Python Type Annotations and Duck Typing

This project aims to explain the following concepts in Python 3:

- **Type Annotations**
- **Function Signatures and Variable Types**
- **Duck Typing**
- **Code Validation with mypy**

---

## 📌 1. Type Annotations

Type annotations allow you to **specify the type of variables or functions** directly in the code.  
Python remains dynamic, so types are not enforced at runtime, but annotations help with readability, code understanding, and catching potential errors.

### Example:
```python
def add(a: int, b: int) -> int:
    return a + b

## 🧩 2. Function Signatures and Variable Types

### Annotated Variables
```python
name: str = "Alice"
age: int = 25
```
### Annotated Functions
```python
def greet(name: str) -> str:
    return "Hello " + name
```
## 🦆 3. Duck Typing

**Duck Typing** means that Python does not check an object’s exact type, but rather its behavior.

*“If it looks like a duck and quacks like a duck, it must be a duck.”*

**Example:**
```python
class Dog:
    def speak(self):
        return "woof"

class Cat:
    def speak(self):
        return "meow"

def animal_sound(animal):
    print(animal.speak())
```

This function works with both Dog and Cat because they both have a speak() method.
Python cares about **what the object can do**, not what type it is.

## 🔍 4. Code Validation with mypy

mypy is a tool that **checks your type annotations** without running your code.

### Installation
```bash
pip install mypy
```
### Checking Your Code
```bash
mypy file.py
```
### Example Error
```python
def add(a: int, b: int) -> int:
    return a + b

result = add(1, "2")
```
### mypy will report:
```error: Argument 2 has incompatible type "str"; expected "int"```

## 🧠 Summary
- **Type Annotations** → Specify types in your code
- **Function Signatures** → Types of parameters and return values
- **Duck Typing** → Python checks behavior, not type
- **mypy** → Automatically verify type correctness