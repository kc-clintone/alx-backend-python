# 0x00-python_variable_annotations

This project focuses on Python variable annotations, providing examples and scripts that demonstrate how to use type hints to improve code readability, maintainability, and error checking. Below is an overview of the scripts in this folder and their functionalities. Happy learning.

## Files and Descriptions

### 0-add.py

- **Description**: Contains a function `add(a: float, b: float) -> float` that adds two floating-point numbers.
- **Example Usage**:
  ```python
  from 0-add import add
  result = add(3.14, 2.71)
  print(result)  # Output: 5.85
  ```

### 1-concat.py

- **Description**: Contains a function `concat(str1: str, str2: str) -> str` that concatenates two strings.
- **Example Usage**:
  ```python
  from 1-concat import concat
  result = concat("Hello, ", "World!")
  print(result)  # Output: Hello, World!
  ```

### 100-safe_first_element.py

- **Description**: Contains a function `safe_first_element(lst: Sequence[Any]) -> Union[Any, None]` that safely retrieves the first element of a sequence, returning `None` if the sequence is empty.
- **Example Usage**:
  ```python
  from 100-safe_first_element import safe_first_element
  result = safe_first_element([1, 2, 3])
  print(result)  # Output: 1
  ```

### 101-safely_get_value.py

- **Description**: Contains a function `safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]` that safely retrieves a value from a dictionary.
- **Example Usage**:
  ```python
  from 101-safely_get_value import safely_get_value
  result = safely_get_value({"a": 1, "b": 2}, "a")
  print(result)  # Output: 1
  ```

### 102-type_checking.py

- **Description**: Demonstrates the use of `mypy` for type checking by simulating various type-annotated functions and structures.
- **Example Usage**:
  ```sh
  mypy 102-type_checking.py
  ```

### 2-floor.py

- **Description**: Contains a function `floor(n: float) -> int` that returns the floor of a floating-point number.
- **Example Usage**:
  ```python
  from 2-floor import floor
  result = floor(3.14)
  print(result)  # Output: 3
  ```

### 3-to_str.py

- **Description**: Contains a function `to_str(n: float) -> str` that converts a float to a string.
- **Example Usage**:
  ```python
  from 3-to_str import to_str
  result = to_str(3.14)
  print(result)  # Output: '3.14'
  ```

### 4-define_variables.py

- **Description**: Demonstrates how to define variables with type annotations.
- **Example Code**:
  ```python
  a: int = 1
  pi: float = 3.14
  is_valid: bool = True
  name: str = "John Doe"
  ```

### 5-sum_list.py

- **Description**: Contains a function `sum_list(input_list: List[float]) -> float` that sums a list of floats.
- **Example Usage**:
  ```python
  from 5-sum_list import sum_list
  result = sum_list([1.1, 2.2, 3.3])
  print(result)  # Output: 6.6
  ```

### 6-sum_mixed_list.py

- **Description**: Contains a function `sum_mixed_list(input_list: List[Union[int, float]]) -> float` that sums a mixed list of integers and floats.
- **Example Usage**:
  ```python
  from 6-sum_mixed_list import sum_mixed_list
  result = sum_mixed_list([1, 2.2, 3])
  print(result)  # Output: 6.2
  ```

### 7-to_kv.py

- **Description**: Contains a function `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]` that returns a tuple.
- **Example Usage**:
  ```python
  from 7-to_kv import to_kv
  result = to_kv("age", 30)
  print(result)  # Output: ('age', 30.0)
  ```

### 8-make_multiplier.py

- **Description**: Contains a function `make_multiplier(multiplier: float) -> Callable[[float], float]` that returns a function that multiplies a float by a given multiplier.
- **Example Usage**:
  ```python
  from 8-make_multiplier import make_multiplier
  multiplier = make_multiplier(2.0)
  result = multiplier(5.0)
  print(result)  # Output: 10.0
  ```

### 9-element_length.py

- **Description**: Contains a function `element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]` that returns a list of tuples with the element and its length.
- **Example Usage**:
  ```python
  from 9-element_length import element_length
  result = element_length(["apple", "banana", "cherry"])
  print(result)  # Output: [('apple', 5), ('banana', 6), ('cherry', 6)]
  ```
