import math

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# Function to find the minimum number of bottles needed
def find_min_bottles(X, bottle1, bottle2, bottle3):
    min_bottles = None
    for i in range(X//bottle3 + 1):
        for j in range((X - i*bottle3)//bottle1 + 1):
            k = (X - i*bottle3 - j*bottle1) // bottle2
            total_bottles = i + j + k
            total_litters = i*bottle3 + j*bottle1 + k*bottle2
            if total_litters == X:
                if min_bottles is None or total_bottles < min_bottles:
                    min_bottles = total_bottles
    return min_bottles

# Example usage
X = 100
bottle1 = 5
bottle2 = 7
bottle3 = 11
min_bottles = find_min_bottles(X, bottle1, bottle2, bottle3)
print("Minimum number of bottles needed:", min_bottles)
