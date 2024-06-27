n = int(input())
moves = []
for i in range(n):
    moves.append(input())

scores_game ={'first': 0, 'second': 0}
scores =0
last_move =''
balls ={'red': 15, 'white': 1, 'black': 1, 'yellow': 1, 'green': 1, 'brown': 1, 'pink': 1, 'blue': 1}

def turn():
    global n
    for i in range(n+1):
        if i%2 == 0:
            yield 'first'
        else:
            yield 'second'
turn_game = turn()
game_turn = next(turn_game)


def check_last_move(last_move:str):
    if last_move == 'red' or balls['red'] ==0:
        return True
    else:
        last_move = ''
        return False

def change_turn(game_t:str ,sco:int):
    scores_game[game_t] += sco
    global scores
    global game_turn
    global last_move
    global balls
    last_move = ''
    scores = 0
    game_turn = next(turn_game)
    if balls['red'] != 0:
        balls.update({'white': 1, 'black': 1, 'yellow': 1, 'green': 1, 'brown': 1, 'pink': 1, 'blue': 1})


def check_ball(color:str):
    if balls[color] !=0:
        return True
    else:
        return False

def reduce_balls(color):
    balls[color] -=1

flag =0
for i in range(n):
    if moves[i] == 'red':
        if check_ball(moves[i]):
            reduce_balls(moves[i])
            scores +=1
            last_move = 'red'
        else:
            print('Invalid')
            flag =1
            break
    elif moves[i] == 'white' or moves[i] == 'miss':
        change_turn(game_turn, scores)
    elif moves[i] == 'green':
        if check_ball(moves[i]):
            if check_last_move(last_move):
                last_move = moves[i]
                scores += 3
                reduce_balls(moves[i])
            else:
                change_turn(game_turn, scores)
        else:
            flag = 1
            print('Invalid')
            break
    elif moves[i] == 'black':
        if check_ball(moves[i]):
            if check_last_move(last_move):
                last_move = moves[i]
                scores += 7
                reduce_balls(moves[i])
            else:
                change_turn(game_turn, scores)
        else:
            flag = 1
            print('Invalid')
            break
    elif moves[i] == 'yellow':
        if check_ball(moves[i]):
            if check_last_move(last_move):
                last_move = moves[i]
                scores += 2
                reduce_balls(moves[i])
            else:
                change_turn(game_turn, scores)
        else:
            flag = 1
            print('Invalid')
            break
    elif moves[i] == 'pink':
        if check_ball(moves[i]):
            if check_last_move(last_move):
                last_move = moves[i]
                scores += 6
                reduce_balls(moves[i])
            else:
                change_turn(game_turn, scores)
        else:
            flag = 1
            print('Invalid')
            break
    elif moves[i] == 'brown':
        if check_ball(moves[i]):
            if check_last_move(last_move):
                last_move = moves[i]
                scores += 4
                reduce_balls(moves[i])
            else:
                change_turn(game_turn, scores)
        else:
            flag = 1
            print('Invalid')
            break
    elif moves[i] == 'blue':
        if check_ball(moves[i]):
            if check_last_move(last_move):
                last_move = moves[i]
                scores += 5
                reduce_balls(moves[i])
            else:
                change_turn(game_turn, scores)
        else:
            flag = 1
            print('Invalid')
            break
    if i == n-1:
        change_turn(game_turn, scores)

if flag ==0:
    if scores_game['first'] > scores_game['second']:
        print('First')
    elif scores_game['first'] < scores_game['second']:
        print('Second')
    else:
        print('Tie')
