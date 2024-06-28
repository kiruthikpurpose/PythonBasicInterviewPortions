def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call to calculate factorial

# Example usage:
if __name__ == "__main__":
    num = 5
    print(f"The factorial of {num} is {factorial(num)}")
