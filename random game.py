import random 
number = random.randint(1,100)
guess = int(input("enter guess number"))
attempts = 1
while number != guess and attempts < 7:
    if guess > number :
        print("too high")
    elif guess < number :
        print("too low")
    guess = int(input("Guess again: "))
    attempts += 1
if number == guess :    
    print("correct you won")
else :
    print("game is over")  
    print(f"correct number is : {number}")   
print(f"Attempts : {attempts}")       