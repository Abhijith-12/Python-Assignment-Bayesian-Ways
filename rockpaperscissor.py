game = int(input('Enter the number of games you want to play ?\n')) 
count1=0
count2=0
for i in range(0,game):
     player1 = input('Enter the player1s choice (rock,paper,scissors as r,p,s respectively) ?\n')
     player2 = input('Enter the player2s choice (rock,paper,scissors as r,p,s respectively) ?\n')
     if (player1=='r') & (player2=='p'):
               count2=count2+1
     elif (player1=='r') & (player2=='s'):
               count1=count1+1
     elif (player1=='p') & (player2=='r'):
               count1=count1+1 
     elif (player1=='p') & (player2=='s'):
               count2=count2+1 
     elif (player1=='s') & (player2=='r'):
               count2=count2+1 
     elif (player1=='s') & (player2=='p'):
               count1=count1+1                
if(count1==count2):
    print("The match ended in draw") 
elif(count1>count2):
    print("The game was won by player 1") 
elif(count1<count2):
    print("The game was won by player 2")                                                         
