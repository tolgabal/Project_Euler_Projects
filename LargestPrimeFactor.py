#The prime factors of 13195 are 5,7,13 and 29. What is the largest prime factor of the number 600851475143?

number = 600851475143
factors = []
primes = []
isPrime = True

for i in range(2,number//2+1):
    if number%i == 0:
        factors.append(i)

totalIndex = len(factors)-1

for i in range(0,totalIndex+1):
    for j in range(2,factors[i]):
        if factors[i]%j == 0 and factors[i] != j:
            isPrime = False
            break
    if isPrime:
        primes.append(factors[i])
    isPrime = True
    
print(primes[len(primes)-1])