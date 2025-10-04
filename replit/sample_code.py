def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("Replit Sample Code Execution")
    print("=" * 40)
    
    print("\nFibonacci sequence (first 10 numbers):")
    print(fibonacci(10))
    
    print("\nFactorial of 5:")
    print(factorial(5))
    
    print("\nPrime numbers between 1 and 20:")
    primes = [num for num in range(1, 21) if is_prime(num)]
    print(primes)
    
    print("\nProgram completed successfully!")
