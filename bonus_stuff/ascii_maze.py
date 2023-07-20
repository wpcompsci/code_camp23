import os

maze = [
    list('######################'),
    list('#### ###   #   # ### #'),
    list('# #   ## # # #     #  '),
    list('# # #    #   ##### # #'),
    list('# # # ########   # # #'),
    list('# # #      #   # # # #'),
    list('#   # ## #   #   #   #'),
    list('######################'),
]

# SET START
x = 2
y = 1

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('###' + maze[x-1][y] * 3 + '###')
    print('###' + maze[x-1][y] * 3 + '###')
    print(maze[x][y-1] * 3 + ' o ' + maze[x][y+1] * 3)
    print('###' + maze[x+1][y] * 3 + '###')
    print('###' + maze[x+1][y] * 3 + '###')

    move = input('w: up, s: down, a: left, d: right ->')
    clear_output()

    if move == 'w':
        if maze[x-1][y] == "#":
            print('Illegal Move!')
        else:
            x -= 1
    elif move == 's':
        if maze[x+1][y] == "#":
            print('Illegal Move!')
        else:
            x += 1
    elif move == 'a':
        if maze[x][y-1] == "#":
            print('Illegal Move!')
        else:
            y -= 1
    elif move == 'd':
        if maze[x][y+1] == "#":
            print('Illegal Move!')
        else:
            y += 1
    elif move == 'h':
        maze[x][y] = 'o'
        for row in maze:
            print(''.join(row))
        maze[x][y] = ' '
        input("Press enter to continue...")
        clear_input()
    elif move == 'q':
        break
        input("Thanks for playing, press enter to close.")
    else:
        print("Not a vaild input!")

    if y == len(maze[0]) - 1:
        print("You made it!")
        input('Press enter to close')
        break
