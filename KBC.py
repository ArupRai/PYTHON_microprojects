import random 
import time 
from os import system
def askquestion(q, o, qnumb) :
    que_index = q.index(random.choice(q))
    print(f"Question no.{qnumb}_ _ on COMPUTER-SCREEN>>>\n{q.pop(que_index)}\n{o.pop(que_index)}")
    return [input(f"Choose [a/b/c/d] or [A/B/C/D]:").lower(), que_index] # return[,] converts tuple->list
def verifyanswer(a,plchoice) : # check answer
    if(a[plchoice[1]] == plchoice[0]) :  return True
    else :  return False
def greetproceed(num) :
    print("drum rolls->>>>>>",end="")
    time.sleep(3)
    if (num == 1) :  print(" HARIII BOOOL...")
    else :  print("NO... you choosed in HURRY BOLO ???")
    time.sleep(2)
    system('cls')
que = ["  Who is Supreme personality of God-head ?", "  How many Shloka and chapters (respectively) are there in Shrimad Bhagwat Geeta ?", "  How many ekadashi we observe yearly ?", "  Chaitanya Mahaprabhu's Mother name was ? "]
opt = ["\tA.xxxx\tB.xxxx\n\tC.xxxx\tD.xxxx", "\tA.xxxx\tB.xxxx\n\tC.xxxx\tD.xxxx", "\tA.xxxx\tB.xxxx\n\tC.xxxx\tD.xxxx", "\tA.xxxx\tB.xxxx\n\tC.xxxx\tD.xxxx"]
ans = ['a','b','c','d']
count = 1
print("\n\n\t\t\t-----HARE KRISHNA-----\n")
player = input("Enter your good name-- ")
system('cls')
print("\t\t\tMain-Menu\n\n\t\tWelcome",player)
if(input("\n\tA->->->Play\t\tB->->->Exit(press any key)\nCHOOSE [a/b] :").lower() == 'a') :
    print("Only 1 rule-->\n!!! answer by yourself !!!\n--->>>YOU WIN or YOU LEARN<<<---\n")
    time.sleep(2)
    system('cls')
    while(True):
        if(len(que) > 0) :
            opt_ans = askquestion(que, opt, count)
            if(verifyanswer(ans, opt_ans)) :
                greetproceed(1)
                count = count + 1           
                if (count == len(ans) + 1) :    break
            else :
                greetproceed(0)
                break
    if(len(que) == 0) :
        print("\n\t\t\t.... ACED ....")
    print(f"{player} gets MERCY X 100 and {count*2} GULAB-JAMUNs\n\n\t\t-----HARE KRISHNA-----\n\n" )