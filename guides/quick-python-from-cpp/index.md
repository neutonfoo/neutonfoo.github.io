---
title: Quick Python from C++
layout: single
---

## #WIP

## Python Files

* Two main versions of Python - `2.7` and `3.x`.
	* It is recommended to use `3.x`, but `2.7` is still heavily used.
	* Can check Python version using `python --version` or `python3 --version`.
* End in `*.py`.
* Run Python programs using `python file.py` or `python3 file.py` in the Terminal.
* Indentation matters.
	* Spaces or tabs are used to create code blocks in lieu of curly braces `{ }`.
	* Cannot mix spaces or tabs, must pick one.
* Semicolons `;` optional.
* Don't need to compile code.

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

```python
x = 100
print(type(x)) # <class 'int'>
y = 1.1
print(type(y)) # <class 'float'>
z = x + y
print(z) # 101.1
print(type(z)) # <class 'float'>

a = "I am a string" # Can also use single quotes ', no difference.
print(type(a)) # <class 'str'>

print(a[0]) # I
print(a[3]) # m
print(a[-1]) # g
```

* Cannot print mixed data types

```python
x = 100

print("x is " + x) # Does not work

print("x is " + str(x)) # Works

print("x is ", end = "") # Also works
print(x)
```

## Conditionals

* Brackets are optional.
* Code block based on colons `:` and indentation. (No curly braces.)
* `||`  to  `or`.
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

## Standard Python File

* Will usually see the `if __name__ == "__main__":` convention.
	* If this file is called from the Terminal, this condition will be `True`.
	* `python3 program.py`.

**program.py**

```python
def main():
	print("Hello")

if __name__ == "__main__": # If this file is run from the terminal
	main()
```

## Python Functions

* No return type needed.
* Using `if __name__ == "__main__":` eliminates need for prototyping.

```python
def main():
	print(power(3, 4))

def power(x, y):
	return x**y # = pow(x, y)

if __name__ == "__main__":
	main()
```

## Loops

```python
def main():
	days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	# No real "arrays" in Python, usually mean list

	for day in days:
		print(day)

	for i in range(len(days)):
		print(days[i])

	for i in range(0, 5):
		print(i)

if __name__ == "__main__":
	main();
```
