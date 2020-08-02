"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""


def get_fib(position):
    if position <= 1:
        return position
    return get_fib(position-1)+get_fib(postion-2)
