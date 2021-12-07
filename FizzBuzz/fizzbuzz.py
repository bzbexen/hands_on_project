liste = list(range(1,101))
for i in liste:
    if i %15 == 0:
        i = "FizzBuzz"
    elif i%3==0 and i%5!=0:
        i = "Fizz"
    elif i%5 == 0 and i%3 !=0:
        i = "Buzz"
    print(i)


