import random
num=random.randrange(1000,10000)
chances=5
guess=int(input(f"Guess a 4 digit number you have{chances} chances left: "))
 
if guess==num:
    print("great you won now you are a mastermind")
else:
    tries=0  
    while guess!=num and chances:
        tries+=1
        chances-=1  
        rightdigit =0
        guess= str(guess)
        num=str(num)
        correct =["X"]*4

        for i in range(0,4):
            if guess[i]==num[i]:
                rightdigit+=1
                correct[i]=num[i]
        if rightdigit < 4 and rightdigit>0 and chances:
            print("not the right guess, but you guessed",rightdigit, "numbers right")  
            print("current status is : ")
            for char in correct :
                print(char,end ='') 
            print('\n')
            print('\n')
            guess=int(input(f"Guess a 4 digit number you have{chances} chances left: "))
        elif rightdigit==0 and chances:  
            print("none of the digit you guessed right")
            guess=int(input(f"Guess a 4 digit number you have{chances} chances left: "))
    if guess ==num:
        print("great you won", tries, "guesses now you are a mastermind")
    if chances==0:
        print("sorry you lost the game, as you run out of chances")
        print("number is", num)    