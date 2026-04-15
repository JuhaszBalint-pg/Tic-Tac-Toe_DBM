#startup, bases
x1 = None
y1 = None
x2 = None
y2 = None
run = True

def rajzX(ui1, ui2):
    tabla[ui1][ui2] = 'X'

def rajzO(ui1, ui2):
    tabla[ui1][ui2] = 'O'

def game_display(tabla):    
    for i in range(0, len(tabla)):
        for j in range(0, len(tabla)):
            if tabla [i][j] == None:
                print('_', end = ' ')
            else:
                print(tabla[i][j], end = ' ')
        print()

def check_winnerO(tabla):
    return((tabla[1]=='O' and tabla[2]== 'O' and tabla[3]=='O' )or

            (tabla[4]=='O' and tabla[5]=='O' and tabla[6]=='O' )or

            (tabla[7]=='O' and tabla[8]=='O' and tabla[9]=='O' )or

            (tabla[1]=='O' and tabla[4]=='O' and tabla[7]== 'O' )or

            (tabla[2]=='O' and tabla[5]=='O' and tabla[8]=='O' )or

            (tabla[3]=='O' and tabla[6]=='O' and tabla[9]=='O' )or

            (tabla[1]=='O' and tabla[5]=='O' and tabla[9]=='O' )or

            (tabla[3]=='O' and tabla[5]=='O' and tabla[7]=='O' ))


def check_winnerX(tabla):
    return((tabla[1]=='X' and tabla[2]== 'X' and tabla[3]=='X' )or

            (tabla[4]=='X' and tabla[5]=='X' and tabla[6]=='X' )or

            (tabla[7]=='X' and tabla[8]=='X' and tabla[9]=='X' )or

            (tabla[1]=='X' and tabla[4]=='X' and tabla[7]== 'X' )or

            (tabla[2]=='X' and tabla[5]=='X' and tabla[8]=='X' )or

            (tabla[3]=='X' and tabla[6]=='X' and tabla[9]=='X' )or

            (tabla[1]=='X' and tabla[5]=='X' and tabla[9]=='X' )or 

            (tabla[3]=='X' and tabla[5]=='X' and tabla[7]=='X' ))



# game
print('Üdvölünk a DBM csapat amőba játékában!')


#irányítás magyarázat
#játékmód választás

#játék
    #játéktábla xx

tabla = [
    [' ', 1, 2, 3],
    ['A', None, None, None],
    ['B', None, None, None],
    ['C' ,None, None, None]
]

    #játéktábla használata
game_display()

print('Az 1. játékos következik')
x1 = input('Add meg a függőleges kordinációt! (A-C)')
if x1 == 'A':
    x1 = 1
elif x1 == 'B':
    x1 = 2
elif x1 == 'C':
    x1 = 3

y1 = int(input('Add meg a vízszinted kordinációt! (1-3)'))

rajzX(x1, y1)


print('Az 2. játékos következik')
x2 = input('Add meg a függőleges kordinációt! (A-C)')
if x2 == 'A':
    x2 = 1
elif x2 == 'B':
    x2 = 2
elif x2 == 'C':
    x2 = 3

y2 = int(input('Add meg a vízszinted kordinációt! (1-3)'))

rajzO(x2, y2)

game_display(tabla)


#winner/loser tab
check_winnerO(tabla)
check_winnerX(tabla)