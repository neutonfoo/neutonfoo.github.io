---
title: Quick Python - Collections
layout: single
sidebar:
  nav: quick-python-basics-collections
---

## Types of Collections

* No real "arrays" in Python like in C++.
* Python has it's own "collection" types.

* **List** - Ordered and mutable. Allows duplicate members.
* **Tuple** - Ordered and unmutable. Allows duplicate members.
* **Set** - Unordered, mutable and unindexed. No duplicate members.
* **Dictionary** - Unordered, mutable and indexed. No duplicate members.

## List

* Collection type most similar to C++ arrays.

```python
l = ["apple", "banana", "cherry"]
# Can also use list constructor list()
# l = list(("apple", "banana", "cherry"))

l[1] = "blackcurrant"

print(l)
```
