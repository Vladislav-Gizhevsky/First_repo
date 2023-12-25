# First code on first repo
print("Hello, World!")

# Factorial func
def factorial(x: int) -> int:
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)