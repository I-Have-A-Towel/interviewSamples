"""
   Q1: Can you describe what this list comprehension is doing?
"""


def double(x):
    return x * 2


val = [double(num) for num in range(1, 10) if num % 2 == 0]

print(val)
