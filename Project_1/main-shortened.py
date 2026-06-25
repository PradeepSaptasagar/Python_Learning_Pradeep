import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([-1,1,0])
youStr=input("Enter your choice: ")
youDict={"S":1,"W":-1,"G":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[youStr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer==you):
    print("Its a draw!")
else:
    '''
    if(computer==-1 and you==1):
        print("You Win!")

    elif(computer==-1 and you==0):
        print("You Lose!")
    
    elif(computer==1 and you==-1):
        print("You Lose!")
    
    elif(computer==1 and you==0):
        print("You Win!")
    
    elif(computer==0 and you==-1):
        print("You Win!")
    
    elif(computer==0 and you==1):
        print("You Lose!")
    
    else:
        print("Something went wrong")

        the below logic is written on the basis of value of commputer-you
    '''
    if((computer-you)==-1 or (computer-you)==2):
        print("You lose!")
    else:
        print("You win!")