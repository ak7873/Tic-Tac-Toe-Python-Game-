import random

print('How To Play:-\n[1-for Top Left, 2-For Top Middle, 3-For Top Right]\
        \n[4-for Middle Left, 5-For Middle Middle, 6-For Middle Right]\
        \n[7-for Low Left, 8-For Low Middle, 9-For Low Right]\nSee Below: ')

print('1'+'|'+'2'+'|'+'3')
print('-+-+-')
print('4'+'|'+'5'+'|'+'6')
print('-+-+-')
print('7'+'|'+'8'+'|'+'9\n')

ans=input('This Game is between YOU & ME(Machine). Do you want to play First? (Yes or No) :-')
print('\n\n:::X- YOUR\n\n:::O-ME\n\nGame has STARTED...')


if ans.lower() == 'yes':

    board = {'1':' ','2':' ','3':' ',
             '4':' ','5':' ','6':' ',
             '7':' ','8':' ','9':' ',}

    def Tic_Tac_Toe(x):
           print(x['1']+'|'+x['2']+'|'+x['3'])
           print('-+-+-')
           print(x['4']+'|'+x['5']+'|'+x['6'])
           print('-+-+-')
           print(x['7']+'|'+x['8']+'|'+x['9'])

    Tic_Tac_Toe(board)

    all_value = []

    machine_move = ['1','2','3','4','5','6','7','8','9']

    for move in range (1):
        n = input('\n\n-> First is your move ( Enter Number) :-')
        machine_move.remove(n)
        board[n] = 'X'
        Tic_Tac_Toe(board)
        all_value.append(n)
        print('\n\n->My Move')
        machine = random.choice(machine_move)
        board[machine] = 'O'
        machine_move.remove(machine)
        all_value.append(machine)
        Tic_Tac_Toe(board)
    
    for move in range (4):
        if move == '3':
            
            while True:
                n = input('\n\n-> your Last Move (Enter Number) :-')
                if n in all_value:
                    print('\n!!Repeated Number!!. Please Enter correct Number')
                    continue
                break
                  
            machine_move.remove(n)
            board[n] = 'X'
            Tic_Tac_Toe(board)
            if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X' \
               or board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X' \
               or board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X' \
               or board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X' \
               or board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X' \
               or board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X' \
               or board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X' \
               or board['3'] == 'X' and board['5'] == 'X' and board['7'] == 'X' :
                            print('..........Yeah!.....YOU WON..........')
                            break
       
            elif board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O' \
                 or board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O' \
                 or board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O' \
                 or board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O' \
                 or board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O' \
                 or board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O' \
                 or board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O' \
                 or board['3'] == 'O' and board['5'] == 'O' and board['7'] == 'O' :
                            print('...OOPS....YOU LOST.  I WON..........')
                            break

        
        while True:
                n = input('\n\n-> your Next Move (Enter Number) :-')
                if n in all_value:
                    print('\n!!Repeated number!!. Please Enter correct Number')
                    continue
                break
        machine_move.remove(n)
        board[n] = 'X'
        Tic_Tac_Toe(board)
        all_value.append(n)
        print('\n\n->My Move')
        machine = random.choice(machine_move)
        board[machine] = 'O'
        machine_move.remove(machine)
        all_value.append(machine)
        Tic_Tac_Toe(board)

        if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X' \
               or board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X' \
               or board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X' \
               or board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X' \
               or board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X' \
               or board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X' \
               or board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X' \
               or board['3'] == 'X' and board['5'] == 'X' and board['7'] == 'X' :
                            print('..........Yeah!.....YOU WON..........')
                            break
       
        elif board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O' \
                 or board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O' \
                 or board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O' \
                 or board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O' \
                 or board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O' \
                 or board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O' \
                 or board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O' \
                 or board['3'] == 'O' and board['5'] == 'O' and board['7'] == 'O' :
                            print('...OOPS....YOU LOST.  I WON..........')
                            break
        continue       
        break

else:
    board = {'1':' ','2':' ','3':' ',
             '4':' ','5':' ','6':' ',
             '7':' ','8':' ','9':' ',}

    def Tic_Tac_Toe(x):
           print(x['1']+'|'+x['2']+'|'+x['3'])
           print('-+-+-')
           print(x['4']+'|'+x['5']+'|'+x['6'])
           print('-+-+-')
           print(x['7']+'|'+x['8']+'|'+x['9'])

    Tic_Tac_Toe(board)
    all_value = []

    machine_move = ['1','2','3','4','5','6','7','8','9']
    
    for move in range (1):
        print('\n\n-> First is My Move')
        machine = random.choice(machine_move)
        board[machine] = 'O'
        machine_move.remove(machine)
        all_value.append(machine)
        Tic_Tac_Toe(board)
        while True:
                n = input('\n\n-> It is your move (Enter Number) :-')
                if n in all_value:
                    print('\n!!Repeated number!!. Please Enter correct Number')
                    continue
                break
        
        board[n] = 'X'
        machine_move.remove(n)
        all_value.append(n)
        Tic_Tac_Toe(board)

    for move in range (4):
        if move == '3':

            machine = random.choice(machine_move)
            
            
            board[machine] = 'O'
            Tic_Tac_Toe(board)
            if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X' \
               or board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X' \
               or board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X' \
               or board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X' \
               or board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X' \
               or board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X' \
               or board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X' \
               or board['3'] == 'X' and board['5'] == 'X' and board['7'] == 'X' :
               
                            print('..........Yeah!.....YOU WON..........')
                            break
       
            elif board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O' \
                 or board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O' \
                 or board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O' \
                 or board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O' \
                 or board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O' \
                 or board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O' \
                 or board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O' \
                 or board['3'] == 'O' and board['5'] == 'O' and board['7'] == 'O' :
        
                            print('..........Yeah!.....YOU WON..........')
                            break
            break
        
        print('\n\n-> My Move')
        machine = random.choice(machine_move)
        board[machine] = 'O'
        machine_move.remove(machine)
        all_value.append(machine)
        Tic_Tac_Toe(board)
        while True:
                n = input('\n\n-> It is your move (Enter Number) :-')
                if n in all_value:
                    print('\n!!Repeated number!!. Please Enter correct Number')
                    continue
                break
        
        board[n] = 'X'
        machine_move.remove(n)
        all_value.append(n)
        Tic_Tac_Toe(board)

        if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X' \
               or board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X' \
               or board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X' \
               or board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X' \
               or board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X' \
               or board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X' \
               or board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X' \
               or board['3'] == 'X' and board['5'] == 'X' and board['7'] == 'X' :
               
                            print('..........Yeah!.....YOU WON..........')
                            break
       
        elif board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O' \
                 or board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O' \
                 or board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O' \
                 or board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O' \
                 or board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O' \
                 or board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O' \
                 or board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O' \
                 or board['3'] == 'O' and board['5'] == 'O' and board['7'] == 'O' :
        
                            print('..........Yeah!.....YOU WON..........')
                            break        
        continue       
        break



    
