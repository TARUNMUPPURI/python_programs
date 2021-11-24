#ROCK PAPER SCISSOR
import random
computer_list=['rock','paper','scissor']
c_score=0
p_score=0
print("THIS GAME WILL ACCEPT EITHER ROCK OR PAPER OR SCISSOR")
print("Dont worry about the case (lower or upper) any thing is fine")
print("TYPE END WHEN YOU WANT TO EXIT THE GAME")
p=input("enter the player input: ").lower()
while p != 'end':
    c = computer_list[random.randint(0,2)]
    #print(c)
    if c=="rock" and p=="paper":
        print("player won this turn")
        p_score += 1
    elif c=="rock" and p=="scissor":
        print("computer won this turn")
        c_score+=1
    elif c=="paper" and p=="rock":
        print("computer won this turn")
        c_score+=1
    elif c=="paper" and p=="scissor":
        print("player won this turn")
        p_score += 1
    elif c=="scissor" and p=="rock":
        print("player won this turn")
        p_score += 1
    elif c=="scissor" and p=="paper":
        print("computer won this turn")
        c_score+=1
    elif c=='paper' and p=='paper':
        print("TIE")
    elif c=='scissor' and p=='scissor':
        print("TIE")
    elif c=='rock' and p=='rock':
        print("TIE")
        
    elif p == 'end':
        break       
    else:
        print("invalid input")
    p=input("enter the player input: ").lower()


print("scores are")
print("players score"+str(p_score))
print("Computer's score"+str(c_score))
