# 0x01-python_async_function

This folder focuses on Python asynchronous programming using `async` and `await` keywords. It contains scripts that demonstrate how to write asynchronous functions, manage concurrency, measure runtime, and handle tasks effectively. Below is an overview of the scripts in this folder and their functionalities.

## Files and Descriptions

### 0-basic_async_syntax.py

- **Description**: Contains a basic example of an asynchronous function `wait_random(max_delay: int = 10) -> float` that waits for a random delay between 0 and `max_delay` seconds and then returns the actual delay.
- **Example Usage**:
  ```python
  import asyncio
  from 0-basic_async_syntax import wait_random

  delay = asyncio.run(wait_random(5))
  print(f"Waited for {delay} seconds")
  ```

### 1-concurrent_coroutines.py

- **Description**: Contains a function `wait_n(n: int, max_delay: int) -> List[float]` that spawns `wait_random` `n` times with the specified `max_delay` and returns the list of all the delays in ascending order.
- **Example Usage**:
  ```python
  import asyncio
  from 1-concurrent_coroutines import wait_n

  delays = asyncio.run(wait_n(5, 5))
  print(f"Delays: {delays}")
  ```

### 2-measure_runtime.py

- **Description**: Contains a function `measure_time(n: int, max_delay: int) -> float` that measures the total runtime for `wait_n` and returns the average time per coroutine.
- **Example Usage**:
  ```python
  import asyncio
  from 2-measure_runtime import measure_time

  average_time = asyncio.run(measure_time(5, 5))
  print(f"Average time per coroutine: {average_time}")
  ```

### 3-tasks.py

- **Description**: Contains a function `task_wait_random(max_delay: int) -> asyncio.Task` that returns a `asyncio.Task` object.
- **Example Usage**:
  ```python
  import asyncio
  from 3-tasks import task_wait_random

  task = task_wait_random(5)
  print(f"Task: {task}")
  ```

### 4-tasks.py

- **Description**: Contains a function `task_wait_n(n: int, max_delay: int) -> List[float]` that spawns `n` tasks using `task_wait_random` and returns the list of delays in ascending order.
- **Example Usage**:
  ```python
  import asyncio
  from 4-tasks import task_wait_n

  delays = asyncio.run(task_wait_n(5, 5))
  print(f"Delays: {delays}")
  ```

