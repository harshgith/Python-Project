import random
import math
l=int(input("enter the lower boound"))
u=int(input("enter the upper bound"))
x=random.randint(l,u)
print("\n\tYou've only ",
       round(math.log(u - l + 1, 2)),
      " chances to guess the integer!\n")
count =0

while count<math.log(u - l + 1, 2):
    count+=1
    
    guess=int(input("enter your guess"))
    
    if x==guess:
        print("you guessed it right in",count,"tries")
        break
    if x>guess:
        print("your guess is two small")
    if x<guess:
        print("your guessn is to big")
    
    if count>math.log(u - l + 1, 2):
          print("\nThe number is %d" % x)
          print("\tGood Luck Next time!")