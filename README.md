# Boring Calculator Module

The Boring Calculator module contains a single class, `Calculator`, that can perform various arithmetic operations on a value stored in memory. The module is designed to work with floating-point numbers.

## Usage

To use the Calculator class, first import the module:

```python
from boring_calculator import Calculator

# For Google Colab you might need to import from main
from boring_calculator import Calculator
```
Then, create an instance of the Calculator class:

```python
calculator = Calculator()
```
By default, the in-memory value is set to 0.0.

## Addition
To add a value to the in-memory value, use the `add(value)` method:
```python
calculator.add(5.0)
```
This will add 5.0 to the in-memory value and return the new value.

## Subtraction
To subtract a value from the in-memory value, use the `subtract(value)` method:
```python
calculator.subtract(3.0)
``` 
This will subtract 3.0 from the in-memory value and return the new value.

## Multiplication
To multiply the in-memory value by a value, use the `multiply(value)` method:
```python
calculator.multiply(4.0)
``` 
This will multiply the in-memory value by 4.0 and return the new value.

## Division
To divide the in-memory value by a value, use the `divide(value)` method:
```python
calculator.divide(2.0)
``` 
This will divide the in-memory value by 2.0 and return the new value.

## Root
To take the nth root of the in-memory value, use the `root(value)` method:
```python
calculator.root(2)
```
This will take the square root of the in-memory value and return the new value.

## Reset
To reset the in-memory value to 0.0, use the `reset()` method:
```python   
calculator.reset()
```
This will reset the in-memory value to 0.0 and return the new value.


## Example

```python
from boring_calculator import Calculator

calculator = Calculator()

calculator.add(5.0)         # returns 5.0
calculator.subtract(3.0)    # returns 2.0
calculator.multiply(4.0)    # returns 8.0
calculator.divide(2.0)      # returns 4.0
calculator.root(2)          # returns 2.0
calculator.reset()          # returns 0.0
```


## Installation

To install the Boring Calculator module, install it from pip:

```shell
pip install boring_calculator
```

## Development

To get started install development dependencies
```shell
pip install -r requirements.txt
```

### Testing
```shell
python -m pytest
```

### Code validation 
```shell
python -m flake8 src
python -m mypy src
```

### Building and publishing
We only publish module in test.pypi.org not to trash the 
real pypi.org

Building and publishing is done by `flit` tool.

```shell
flit publish --repository pypitest
```