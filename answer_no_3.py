def fibonacci_sum(x, y, n):
    if n < 3:
        return 0, 0
    
    fib = [x, y]
    even_sum = 0
    odd_sum = y
    
    for i in range(2, n):
        fib_i = fib[i-1] + fib[i-2]
        if fib_i % 2 == 0:
            even_sum += fib_i
        else:
            odd_sum += fib_i
        fib.append(fib_i)
    
    return even_sum, odd_sum

x = 2
y = 3
n = 3

even_sum, odd_sum = fibonacci_sum(x, y, n)

print("Fibonacci sequence from {} and {}:".format(x, y))
for i in range(n):
    print(fib[i], end=" ")
print("\nSum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
