import random
#guess num
r = random.randint(1,100)
times = 0
while True:
    times += 1
    ans = int(input("Please guess the number"))
    #ans =int(ans)
    if ans == r:
        print("You are right")
        break
    elif ans > r:
        print("Too much, please try again")
    elif ans < r:
        print("Fewer,plase try again")
print("for",times,"times")