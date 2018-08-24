---
title: Quick Python - Basics
layout: single
sidebar:
  nav: quick-python-basics-nav
---

## Python

* Two main versions of Python - `2.7` and `3.x`.
	* It is recommended to use `3.x`, but `2.7` is still heavily used and supported.
	* Can check Python version using `python --version` or `python3 --version`.
* Python files have the `*.py` extension.
* Run Python programs using `python file.py` or `python3 file.py` in the Terminal.
* Indentation matters.
	* Spaces or tabs are used to create code blocks in lieu of curly braces `{ }`.
	* Cannot mix spaces or tabs, must pick one.
* Semicolons `;` optional.
* Don't need to compile code like in `C++`;
* Look into [Anaconda](https://www.anaconda.com/download/) if using Python for data science.

## Printing

In C++

```cpp
std::cout << "Hello";
std::cout << " World" << std::endl;

std::cout << "New" << std::endl;
std::cout << "Line" << std::endl;
```

In Python

```python
print("Hello", end = " ") # Must use `end =` if you want everything on one line.
print("World")

print("New") # Automatically puts a new line
print("Line")
```

## Variables

* No need to declare type (type is inferred).
* Most common variable types: `int`, `float`, `string`
	* Python also supports `complex` numbers: `c = 1 + 2j`

```python
x = 100
print(type(x)) # <class 'int'>
y = 1.1
print(type(y)) # <class 'float'>
z = x + y
print(z) # 101.1
print(type(z)) # <class 'float'>

c = 3 + 5j # Python supports complex numbers
print(c * 2) # (6+10j)
print(type(z)) # <class 'complex'>

a = "I am a string" # Can also use single quotes ', no difference.
print(type(a)) # <class 'str'>

print(a[0]) # I
print(a[3]) # m
print(a[-1]) # g
```

* Cannot print mixed data types.

```python
x = 100

print("x is " + x) # Does not work

print("x is " + str(x)) # Works

print("x is ", end = "") # Also works
print(x)
```

## Casting

* `int()`, `float()` and `str()`.

```python
x = int(1.9) # x = 1
y = int('5.2') # y = 5
z = float('5.2') # z = 5.2

a = str(2)    # y = '2'
b = str(3.0)  # z = '3.0'
```

## Arithmetic and Assignment Operators

* Generally the same as the ones in C++.
	* `+`, `-`, `*`, `/`, `%`
	* `+=`, `-=`, `*=`, `/=`, `%=`
* Exponential is `**`: `2**3` = `pow(2,3)`
* Floor division is `//`: `3//2` = `floor(3/2)`


## Logical Operators and Conditionals

* Brackets are optional.
* Code block based on colons `:` and indentation. (No curly braces.)
* `||`  to  `or`.
* `!(__condition__)` to `not __condition__`
* `&&`  to  `and`.
* `else if`  to  `elif`.
* `true`  to  `True`.
* `false`  to  `False`.

In C++

```cpp
int x = 100;
int y = 50;

if(x > y) {
	std::cout << "x is greater than y" << std::endl;
} else if(x < y) {
	std::cout << "y is greater than x" << std::endl;
} else {
	std::cout << "x is equal to y" << std::endl;
}

int a = 1;
int b = 1;
int c = 1;

if(a == b and a == c) {
	std::cout << "a is equals to b and c" << std::endl;
}

if(a == 1 || b == 1 || c == 1) {
	std::cout << "a, b or c equals 1" << std::endl;
}
```

In Python

```python
x = 100;
y = 50;

if x > y:
	print('x is greater than y')
elif x < y:
	print('y is greater than x')
else:
	print('x is equal to y')

a = 1
b = 1
c = 1

if a == b and a == c:
	print('a is equals to b and c')

if a == 1 or b == 1 or c == 1:
	print('a, b or c equals 1')
```

## For Loops

* `for` loops in Python work differently from `for` loops in other languages.
* Works more like an iterator.
	* Similar to a `foreach` loop.

```python
for i in range(0, 5): # Loops through 0 to 4
	print(i)
```

## Python Files

* Will usually see the `if __name__ == "__main__":` convention.
	* If this file is called from the Terminal, this condition will be `True`.
	* `python3 program.py`.
* Main code will be in the `main()` function.

`program.py`

```python
def main():
	print("Hello")

if __name__ == "__main__": # If this file is run from the terminal
	main()
```

## Functions

* No return type needed.
* Using `if __name__ == "__main__":` eliminates need for prototyping.

```python
def main():
	print(power(3, 4))

def power(x, y):
	return x**y

if __name__ == "__main__":
	main()
```
