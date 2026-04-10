# 📘 Python - Async Comprehension

## 📌 Description

This module implements an asynchronous generator in Python.
It allows producing a sequence of values asynchronously, using the `async and `await` keywords.

---

## 🎯 Objective

The goal is to understand:

- **Asynchronous functions** (`async def`)
- The use of `await`
- The concept of an **asynchronous generator* (`yield` in an async function)
- Time management with `asyncio`

---

## ⚙️ Functionality

The file contains a function:

```python
async def async_generator():
```
**This function:**
- Waits 1 second on each iteration (`await asyncio.sleep(1)`)
- Generates a random number
- Repeats this 10 times
- Uses `yield` to return each value

## 🧠 Key Concepts
**🔹 Asynchronous Function**
A function defined with async def allows code to run non-blocking.

```python
async def my_function():
    await asyncio.sleep(1)
```

### 🔹 await
The await keyword lets you wait for an asynchronous operation without blocking the program.

### 🔹 Asynchronous Generator

An asynchronous generator is a function that uses:
```python
async def
yield
```
👉 This allows producing values one by one in an asynchronous context.

### 🔹 asyncio
The asyncio module allows managing asynchronous tasks in Python.

**Example :**

import asyncio
await asyncio.sleep(1)
▶️ Exemple d’utilisation
import asyncio
```python
async def main():
    async for value in async_generator():
        print(value)

asyncio.run(main())
```

---

## 📈 Behavior
The program prints a random number every second
It runs without blocking other asynchronous tasks

---

## 🧩 Use Cases
**Asynchronous generators are useful for:**
- Reading data streams
- Processing APIs incrementally
- Handling large volumes of data without loading everything into memory

---

## 📚 Resources
- DOfficial Python documentation: asyncio
- PEP 525 – Asynchronous Generators
