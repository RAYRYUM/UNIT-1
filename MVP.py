import sys
import time
import timeit
import os
from timeit import default_timer as timer

score=0

start = timer()
print("Hello player!")
time.sleep(1)
name=input("What is your name? ")
time.sleep(0.6)
print('Welcome to game 161!')
time.sleep(0.6)
print('Please answer each answer with a number.')
time.sleep(0.6)
answer=input('are you ready to start the game? (yes/no)')

if answer.lower()=='yes':
    print("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░██░░██░░░░░██░░██░░░░░██░░██░░░░░
░░░░██████░░░░░██████░░░░░██████░░░░░
░░░████████░░░████████░░░████████░░░░
░░░██░██░██░░░██░██░██░░░██░██░██░░░░
░░░████████░░░████████░░░████████░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")
    time.sleep(1)
    q1=input("How many rabbits are there on the screen?")
    if q1.lower()=='3':
        time.sleep(1)
        print('Correct answer!')
        score += 1
    else:
        time.sleep(1)
        print('Wrong answer... How did you get that wrong?')

    time.sleep(1)
    print('Next question!')
    time.sleep(1)
    print("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░██░░██░░░░░██░░██░░░░░██░░██░░░░░
░░░░██████░░░░░██████░░░░░██████░░░░░
░░░████████░░░████████░░░████████░░░░
░░░████████░░░██▒██▒██░░░████████░░░░
░░░████████░░░████████░░░████████░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")
    q2=input('How many rabbits have their eyes open?')
    if q2.lower()=='1':
        time.sleep(1)
        print('Correct answer!')
        score += 1
    else:
        time.sleep(1)
        print("Wrong answer... Did you do this with your eyes closed?")
    time.sleep(1)
    print('Next question!')
    time.sleep(1)
    print("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░██░░██░░░░░██░░██░░░░░
░░░░░░░░░░░░░░░██████░░░░░██████░░░░░
░░░░░░░░░░░░░░████████░░░████████░░░░
░░░░░░░░░░░░░░██▒██▒██░░░██░██░██░░░░
░░░░░░░░░░░░░░████████░░░████████░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")
    q3=input('How many bunnies are there on the screen?')
    if q3.lower()=='2':
        time.sleep(1)
        print('Correct answer!')
        score += 1
    else:
        time.sleep(1)
        print("Wrong answer... The first one is clearly gone though..?")
    end = timer()
    etime = (int(end - start))
    time.sleep(1)
    print('Congrats! You finished the game',name+'!')
    time.sleep(1)
    print('You finished the game in',etime,'seconds with a score of',score,'out of 3!')
    time.sleep(1)
    if score==3:
        print("Great job",name+"! You input all the right answers!")
    elif score==2:
        print("Almost..? I hope that was just a typo!")
    elif score==1:
        print(name+'... How did you manage this?')
    else:
        print('Congrats you somehow got everything wrong! That takes effort',name+'.')
    time.sleep(1)
    print('Thanks for playing!')
elif answer.lower()=='no':
    time.sleep(1)
    print('Bye then!')
    sys.exit()
else:
    print('INVALID ANSWER - PLEASE RESTART PROGRAM')

