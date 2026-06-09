
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

sum_of_primes = 0

for num in range(start, end + 1):
    if num > 1:
        count = 0
        
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
                
        if count == 2:   
            print(num)
            sum_of_primes += num

print("Sum of prime numbers:", sum_of_primes)