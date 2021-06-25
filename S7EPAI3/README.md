# Scopes and Closures

### Create a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable
### Solution
```
def docstringLengthChecker(input_fn, max_doc_len=50)
```
This function take two arguments. The first one is the function for which the length must be checked and the second argument is the max size of the docstring(default is 50). The `max_doc_len` is used as free variable. For `input_fn` we first check if it has a non-null docstring length and then validate against the configured docstring value.

### Create a closure that gives you the next Fibonacci number
### Solution
```
def generateFibo(start_val=1)
```
This closure take an optional parameter as start of Fibonacci series . The input value must be a Fibonacci number else the series is initialized to 1. This validated value is stored as a free variable of the closure and is set to the next Fibonacci number on every call.

### Create a closure that returns 3 functions add,mul and div and keeps track of each function call independently and updates a global counter
### Solution:
```
def accounterOperations()
```
This closure will internally maintain 3 independent free variables `adder_call_count, multiplier_call_count and divider_call_count`. Each of these variables is incremented when the relevant function is called

### Modify above such that now we can pass in different dictionary variables to update different dictionaries 
### Solution:

```
def accntrOperations(accnt_dict)
```
This closure performs same functionality as above however it accepts a user-defined dictionary as an input variable which is maintained then as a free variable.


