def collatz(num):
    if num % 2 == 0:
        print(num//2)
        return num//2
    if num % 2 == 1:
        print(3 * num + 1)
        return 3 * num + 1
repeat = True
while (repeat): 
    try:
        user_num = int(input("Enter an integer\n"))
        while(user_num != 1):
            user_num = collatz(user_num)
        repeat = False
    except ValueError:
        print("That is not an integer.")
        repeat = True