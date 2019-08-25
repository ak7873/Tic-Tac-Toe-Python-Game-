
@author: Alok_Aryan_
"""

import random
print('''How To Play:- 
      #Location
      [1-for Top Left, 2-For Top Middle, 3-For Top Right]
      [4-for Middle Left, 5-For Middle Middle, 6-For Middle Right]
      [7-for Low Left, 8-For Low Middle, 9-For Low Right]
      
      See Below:-''')


print('''\n
     1 | 2 | 3
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9 
    ''')

ans=input('''This Game is between YOU & ME(Machine).
Do you want to play First? (Yes or No) :-''')

print('''\n  X - YOUR
  O - ME
  Game has STARTED...\n''')


board = {'1':' ','2':' ','3':' ',
         '4':' ','5':' ','6':' ',
         '7':' ','8':' ','9':' ',}

random_num=['1','2','3','4','5','6','7','8','9']

def print_board():
    
           print(' '+board['1']+' '+'|'+' '+board['2']+' '+'|'+' '+board['3']+' ')
           print('---+---+---')
           print(' '+board['4']+' '+'|'+' '+board['5']+' '+'|'+' '+board['6']+' ')
           print('---+---+---')
           print(' '+board['7']+' '+'|'+' '+board['8']+' '+'|'+' '+board['9']+' ')

    
print_board()    

if ans.lower()=='yes' or ans.lower()=='y':
    
    all=[]
    i=0
    while i <10:
        
        #user-------------------
        user_input=str(input("\nYour move ( Enter number ) :-"))
        if user_input in all or len(user_input)>1:
            print("\nYou entered wrong number.Try Again...")
            continue
        board[user_input]='X'
        all.append(user_input)
        random_num.remove(user_input)
        print_board()
        if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X' \
            or board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X' \
            or board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X' \
            or board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X' \
            or board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X' \
            or board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X' \
            or board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X' \
            or board['3'] == 'X' and board['5'] == 'X' and board['7'] == 'X' :
                
                print("~~~~You WON~~~~~")
                break
        i+=1
        if i==9:
            print("\n--- no winner ----")
            break
        #Machine-------
        print('\nMy Move:- \n')
        computer_input=random.choice(random_num)
        all.append(computer_input)
        board[computer_input]='O'
        random_num.remove(computer_input)
        print_board()
        if board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O' \
            or board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O' \
            or board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O' \
            or board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O' \
            or board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O' \
            or board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O' \
            or board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O' \
            or board['3'] == 'O' and board['5'] == 'O' and board['7'] == 'O' :
                print("~~~~oops You Lost~~~~~")
                break
                

        i+=1
    


    
    
elif ans.lower()=='no' or ans.lower()=='n':
       
    all=[]
    i=0
    while i <10:
        
        #Machine-------
        print('\nMy Move:- \n')
        computer_input=random.choice(random_num)
        all.append(computer_input)
        board[computer_input]='O'
        random_num.remove(computer_input)
        print_board()
        if board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O' \
            or board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O' \
            or board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O' \
            or board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O' \
            or board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O' \
            or board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O' \
            or board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O' \
            or board['3'] == 'O' and board['5'] == 'O' and board['7'] == 'O' :
                print("~~~~oops You Lost~~~~~")
                break
        i+=1
        if i==9:
            print("\n--- no winner ----")
            break
         #user-------------------
        while True:
            user_input=str(input("\nYour move ( Enter number ) :-"))
            if user_input in all or len(user_input)>1:
                print("\nYou entered wrong number.Try Again...")
                continue
            break
        board[user_input]='X'
        all.append(user_input)
        random_num.remove(user_input)
        print_board()
        if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X' \
            or board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X' \
            or board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X' \
            or board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X' \
            or board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X' \
            or board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X' \
            or board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X' \
            or board['3'] == 'X' and board['5'] == 'X' and board['7'] == 'X' :
                
                print("~~~~You WON~~~~~")
                break
       
                

        i+=1
        

