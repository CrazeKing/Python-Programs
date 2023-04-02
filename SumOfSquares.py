#Function declaration
def squares_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num * num
    return sum
        
numbers = [1, 2, 3, 4, 5, 6, 7]

#Calling function
result = squares_sum(numbers)

#Output will be 140
print("The Result is:",result)
