#Taking users input
num = int(input("Enter a Number: "))

#Check if the number is divisible by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")

#Check if the number is divisible by 3
elif num % 3 == 0:
    print("Fizz")

#Check if the number is divisible by 5
elif num % 5 == 0:
    print("Buzz")
#If none matches print else part
else:
    print(num,"is not divisible by 3 or 5")
