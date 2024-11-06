# range() vs xrange()
# deep copy vs shallow copy


Here’s a simple example demonstrating the difference between **shallow copy** and **deep copy** in Python using the `copy` module. I'll also show the operations you can perform to understand how both copies behave:

```python
import copy

# Original list containing mutable objects (a list inside a list)
original_list = [[1, 2, 3], [4, 5, 6], 7, 8]

# Perform a shallow copy
shallow_copy_list = copy.copy(original_list)

# Perform a deep copy
deep_copy_list = copy.deepcopy(original_list)

# Let's modify the original list and see how it affects the copies
original_list[0][0] = 100  # Modify the inner list
original_list[2] = 700     # Modify an element in the outer list

# Print the original and both copied lists
print("Original list:", original_list)
print("Shallow copy list:", shallow_copy_list)
print("Deep copy list:", deep_copy_list)
```

### Explanation:
1. **Original list** contains nested lists and simple integers.
2. **Shallow copy (`copy.copy()`)**: It creates a new outer list but does not create copies of nested objects (references are copied). Thus, changes to nested objects in the original list will reflect in the shallow copy.
3. **Deep copy (`copy.deepcopy()`)**: It creates a completely new copy of the original list and all of its objects, even nested ones. Changes to the original list (including nested objects) do not affect the deep copy.

### Output:
```
Original list: [[100, 2, 3], [4, 5, 6], 700, 8]
Shallow copy list: [[100, 2, 3], [4, 5, 6], 7, 8]
Deep copy list: [[1, 2, 3], [4, 5, 6], 7, 8]
```

### Key Observations:
- **Shallow copy** (`shallow_copy_list`): Changes to the inner list (`[100, 2, 3]`) are reflected in the shallow copy, but the outer list modification (`700` instead of `7`) does not affect it.
- **Deep copy** (`deep_copy_list`): No changes in the deep copy because it maintains completely independent copies of both the outer and inner lists.

This example helps clarify how shallow and deep copies behave when you modify mutable objects like lists inside other lists.
