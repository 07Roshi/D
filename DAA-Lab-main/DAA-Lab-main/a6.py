def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i - 1] + fib_series[i - 2])
    return fib_series


num = int(input("Enter the number: "))
fibonacci_series = fibonacci(num)
print("Fibonacci series for", num, ":", fibonacci_series)
