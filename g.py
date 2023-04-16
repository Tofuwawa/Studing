import random
#guess num
minn = int(input("Please type the min number"))
maxx = int(input("Please type the max number"))
r = random.randint(minn,maxx)
print("Now the random range is",minn,"to",maxx)
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