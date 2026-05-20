#startup, bases

run = True

def rajzX(tabla, ui1, ui2):
    tabla[ui1][ui2] = 'X'

def rajzO(tabla, ui1, ui2):
    tabla[ui1][ui2] = 'O'

def game_display(tabla):    
    for sor in range(0, len(tabla)):
        for oszlop in range(0, len(tabla)):
            if tabla [sor][oszlop] == None:
                print('_', end = ' ')
            else:
                print(tabla[sor][oszlop], end = ' ')
        print()

def check_winnerO(board):
    if  ((board[1][1]=='O' and board[1][2]== 'O' and board[1][3]=='O' )or

            (board[2][1]=='O' and board[2][2]=='O' and board[2][3]=='O' )or

            (board[3][1]=='O' and board[3][2]=='O' and board[3][3]=='O' )or

            (board[1][1]=='O' and board[2][1]=='O' and board[3][1]== 'O' )or

            (board[1][2]=='O' and board[2][2]=='O' and board[3][2]=='O' )or

            (board[1][3]=='O' and board[2][3]=='O' and board[3][3]=='O' )or

            (board[1][1]=='O' and board[2][2]=='O' and board[3][3]=='O' )or

            (board[1][3]=='O' and board[2][2]=='O' and board[3][1]=='O' )):
        return True


def check_winnerX(board):
    if  ((board[1][1]=='X' and board[1][2]== 'X' and board[1][3]=='X' )or

        (board[2][1]=='X' and board[2][2]=='X' and board[2][3]=='X' )or

        (board[3][1]=='X' and board[3][2]=='X' and board[3][3]=='X' )or

        (board[1][1]=='X' and board[2][1]=='X' and board[3][1]== 'X' )or

        (board[1][2]=='X' and board[2][2]=='X' and board[3][2]=='X' )or

        (board[1][3]=='X' and board[2][3]=='X' and board[3][3]=='X' )or

        (board[1][1]=='X' and board[2][2]=='X' and board[3][3]=='X' )or

        (board[1][3]=='X' and board[2][2]=='X' and board[3][1]=='X' )):
        return True
    
def check_draw(board):
    if board[1][1] and board[1][2] and board[1][3] and board[1][2] and board[2][2] and board[2][3] and board[3][1] and board[3][1] and board[3][3] != None:
        return True
    else: return False

# game
print('Üdvölünk a DBM csapat amőba játékában!')


#irányítás magyarázat

#játék
    #játéktábla xx
tabla = []

info_sor = ['', 1, 2 ,3]
tabla.append(info_sor)
a = ['A', None, None, None]
tabla.append(a)
b = ['B', None, None, None]
tabla.append(b)
c = ['C', None, None, None]
tabla.append(c)


    #játéktábla használata
Run = True
while Run:
    x1 = None
    o1 = None
    x2 = None
    o2 = None


    print('Az 1. játékos következik')
    x1 = input('Add meg a függőleges kordinációt! (A-C)\n').capitalize()
    if x1 == 'A':
        x1 = 1
    elif x1 == 'B':
        x1 = 2
    elif x1 == 'C':
        x1 = 3
    else:
        print('Nincsen ilyen betükordináció!')

    x2 = int(input('Add meg a vízszinted kordinációt! (1-3)\n'))   
#    if x2 != 1 or x2 != 2 or x2 != 3:
#        print('Nincsen ilyen számkordináció!')

    rajzX(tabla, x1, x2)
    game_display(tabla)
    print(' ')

    outcome1 = check_winnerO(tabla)
    outcome2 = check_winnerX(tabla)
    outcome3 = check_draw(tabla)

    if outcome1 == True:
        print('A játékot megnyerte: P1')
        regame = input('Szeretnél tovább játszani? I/N\n').capitalize()
        if regame == 'I':
            print('Új játék!')
            continue
        if regame == 'N':
            print('Köszönjük a játékot!')
            break

    elif outcome2 == True:
        print('A játékot megnyerte: P2')
        regame = input('Szeretnél tovább játszani? I/N\n').capitalize()
        if regame == 'I':
            print('Új játék!')
            continue
        if regame == 'N':
            print('Köszönjük a játékot!')
            break   

    elif outcome3 == True:
        print('Döntetlen! Egyik játékos sem nyert!')
        regame = input('Szeretnél tovább játszani? I/N\n').capitalize()
        if regame == 'I':
            print('Új játék!')
            continue
        if regame == 'N':
            print('Köszönjük a játékot!')
            break


    print('Az 2. játékos következik')
    o1 = input('Add meg a függőleges kordinációt! (A-C)\n').capitalize()
    if o1 == 'A':
        o1 = 1
    elif o1 == 'B':
        o1 = 2
    elif o1 == 'C':
        o1 = 3
    else:
        print('Nincsen ilyen betükordináció!')

    o2 = int(input('Add meg a vízszinted kordinációt! (1-3)\n'))
#    if o2 != 1 or o2 != 2 or o2 != 3:
#        print('Nincsen ilyen számkordináció!')


    rajzO(tabla, o1, o2)

    game_display(tabla)
    print(' ')

 
 
    #winner/loser tab
    outcome1 = check_winnerO(tabla)
    outcome2 = check_winnerX(tabla)
    outcome3 = check_draw(tabla)

    if outcome1 == True:
        print('A játékot megnyerte: P1')
        regame = input('Szeretnél tovább játszani? I/N\n').capitalize()
        if regame == 'I':
            print('Új játék!')
            continue
        if regame == 'N':
            print('Köszönjük a játékot!')
            break

    elif outcome2 == True:
        print('A játékot megnyerte: P2')
        regame = input('Szeretnél tovább játszani? I/N\n').capitalize()
        if regame == 'I':
            print('Új játék!')
            continue
        if regame == 'N':
            print('Köszönjük a játékot!')
            break   

    elif outcome3 == True:
        print('Döntetlen! Egyik játékos sem nyert!')
        regame = input('Szeretnél tovább játszani? I/N\n').capitalize()
        if regame == 'I':
            print('Új játék!')
            continue
        if regame == 'N':
            print('Köszönjük a játékot!')
            break