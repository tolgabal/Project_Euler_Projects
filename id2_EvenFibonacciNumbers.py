#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

even_sum = 2
numbers = [1,2]
i = 1

while True:
    if i%2 == 1:
        numbers[0] += numbers[1]
        i += 1
        if numbers[0] >= 4000000:
            break
        elif numbers[0]%2 == 0:
            even_sum += numbers[0]
    else:
        numbers[1] += numbers[0]
        i += 1
        if numbers[1] >= 4000000:
            break
        elif numbers[1]%2 == 0:
            even_sum += numbers[1]
            
print(even_sum)