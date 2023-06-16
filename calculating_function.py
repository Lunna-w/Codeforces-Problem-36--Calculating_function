n = int(input())

def func(n):
    evens = n // 2  
    odds = n - evens  
    total = evens * (evens + 1) - odds * odds
    return total

print(func(n))