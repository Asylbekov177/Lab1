import random
print("Hello! What is your name?")
name=input()

attempts=0

num = random.randint(1, 20)
print("Well, KBTU, I am thinking of a number between 1 and 20.")
print("Take a guess")

tr = 0
while(tr!=num):
    tr=int(input())
    if(tr<num):
        print("Your guess is too low.")
        print("Take a guess")
        attempts+=1

    elif(tr>num):
        print("Your guess is too high.")
        print("Take a guess")
        attempts+=1

    else:
        attempts+=1
        print("Good job, {fname}! You guessed my number in {fattempt} guesses!".format(fname = name, fattempt = attempts))
        break