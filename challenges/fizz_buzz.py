i = 100
j = 0

while (j<i):
    j = j+1
    
    if (j%3 == 0 and j%5 == 0):
        print(str(j) + " FizzBuzz!")

    elif (j%3 == 0):
        print(str(j) + " Fizz!")

    elif (j%5 == 0):
        print(str(j) + " Buzz!")