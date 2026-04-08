# Asyncio & Random Project

This project demonstrates the use of **Python asynchronous programming** with `asyncio` and `random`. By the end of this project, you should be able to:

- Understand `async` and `await` syntax
- Execute an async program using `asyncio`
- Run concurrent coroutines
- Create asyncio tasks
- Use the `random` module

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Examples](#examples)
4. [Explanation](#explanation)
5. [License](#license)

## Installation

Make sure you have Python 3.7+ installed. Then, clone this repository:

```bash
git clone https://github.com/yourusername/asyncio-random-project.git
cd asyncio-random-project
```

## Usage
```bash
Run the main program:
python main.py
```

## Examples
**Running a simple coroutine**
```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())
```

## Running multiple coroutines concurrently
```python
import asyncio
import random

async def random_sleep(name):
    t = random.uniform(0.5, 2)
    await asyncio.sleep(t)
    print(f"{name} slept for {t:.2f} seconds")

async def main():
    await asyncio.gather(random_sleep("Task 1"), random_sleep("Task 2"))

asyncio.run(main())
```

## Creating asyncio tasks
```python
import asyncio

async def say(number):
    await asyncio.sleep(1)
    print(f"Hello {number}")

async def main():
    task1 = asyncio.create_task(say(1))
    task2 = asyncio.create_task(say(2))

    print("Tasks created")
    await task1
    await task2

asyncio.run(main())
```

## Explanation
- async def → defines a coroutine
- await → waits for a coroutine to finish without blocking
- asyncio.run() → runs the main coroutine
- asyncio.gather() → runs multiple coroutines concurrently
- asyncio.create_task() → schedules a coroutine as a task
- random → used to generate random numbers or delays