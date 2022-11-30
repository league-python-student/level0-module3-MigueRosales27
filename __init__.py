
if __name__ == '__main__':
    print("new line 1 ")
    for i in range(21):

        if (i % 5 == 0 & i % 3 == 0):
            print("Fizz Buzz!")
        elif(i%3==0):
            print("Fizz")

        elif(i%5==0):
            print("Buzz")

        else:
            print(i)