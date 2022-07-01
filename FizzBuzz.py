for x in range(0, 101):
    if (x%15 == 0):
        print("FizzBuzz")
        #this replaces numbers which are multiples of both three and five and prints "FizzBuzz"
    elif (x%3 == 0):
        print("Fizz")
        #this replaces numbers which are multiples of three and prints "Fizz"
    elif (x%5 == 0):
        print("Buzz")
         #this replaces numbers which are multiples of five and prints "Buzz"
    else:
        print(x)
         #this prints numbers if they do not meet the other requirments. 
