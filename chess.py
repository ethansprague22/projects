# Initial board position
board = []
for i in range(64):
    board.append('  ')
for i in range(8,16):
    board[i] = 'P+'
for i in range(48, 56):
    board[i] = 'P-'

board[0] = 'R+'
board[1] = 'N+'
board[2] = 'B+'
board[3] = 'Q+'
board[4] = 'K+'
board[5] = 'B+'
board[6] = 'N+'
board[7] = 'R+'
board[56] = 'R-'
board[57] = 'N-'
board[58] = 'B-'
board[59] = 'Q-'
board[60] = 'K-'
board[61] = 'B-'
board[62] = 'N-'
board[63] = 'R-'

# 56 57 58 59 60 61 62 63
# 48 49 50 51 52 53 54 55
# 40 41 42 43 44 45 46 47
# 32 33 34 35 36 37 38 39
# 24 25 26 27 28 29 30 31
# 16 17 18 19 20 21 22 23
#  8  9 10 11 12 13 14 15
#  0  1  2  3  4  5  6  7

# Converts coord notation into [0,63] notation      
def get_tile(x):    # 8(rank) + file               
    lets = ['a','b','c','d','e','f','g','h']       
    nums = ['1','2','3','4','5','6','7','8']       
    for i in lets:                                 
        if i == x[0]:                              
            return (8 * nums.index(x[1])) + lets.index(x[0])              

def get_legal(x):   # return set of legal tiles given input tile, x is a number
    if board[x] == 'P+':
        # if on home row, can move 2
        # if no piece in front, can move forward
        # if piece on diag, can capture
        # make list of all moves, then delete invalid ones
        legals = []
        if board[x+8] == '  ':
            legals.append(x+8)
        if 8 <= x and x <= 15:
            if board[x+16] == '  ':
                legals.append(x+16)
        if board[x+7] != '  ':
            legals.append(x+7)
        if board[x+9] != '  ':
            legals.append(x+9)
        return legals
        
    if board[x] == 'P-':
        legals = []
        if board[x-8] == '  ':
            legals.append(x-8)
        if 48 <= x and x <= 55:
            if board[x-16] == '  ':
                legals.append(x-16)
        if board[x-7] != '  ':
            legals.append(x-7)
        if board[x-9] != '  ':
            legals.append(x-9)
        return legals

    #if board[x][0] == 'R':
        
        
def make_move():
    move = input("Input move: ")
    grab = move[0:2]
    drop = move[3:5]
    board[get_tile(drop)] = board[get_tile(grab)]
    board[get_tile(grab)] = '  '

    #if get_tile(drop) in get_legal(get_tile(grab)):
        #board[get_tile(drop)] = board[get_tile(grab)]
        #board[get_tile(grab)] = '  '

def print_board():
    line = '+--+--+--+--+--+--+--+--+'
    row1 = ''
    row2 = ''
    row3 = ''
    row4 = ''
    row5 = ''
    row6 = ''
    row7 = ''
    row8 = ''
    for i in range(56,64):
        row1 = row1 + '|' + board[i]
    row1 = row1 + '|'
    for i in range(48,56):
        row2 = row2 + '|' + board[i]
    row2 = row2 + '|'
    for i in range(40,48):
        row3 = row3 + '|' + board[i]
    row3 = row3 + '|'
    for i in range(32,40):
        row4 = row4 + '|' + board[i]
    row4 = row4 + '|'
    for i in range(24,32):
        row5 = row5 + '|' + board[i]
    row5 = row5 + '|'
    for i in range(16,24):
        row6 = row6 + '|' + board[i]
    row6 = row6 + '|'
    for i in range(8,16):
        row7 = row7 + '|' + board[i]
    row7 = row7 + '|'
    for i in range(0,8):
        row8 = row8 + '|' + board[i]
    row8 = row8 + '|'
    print('\n')
    print(line)
    print(row1)
    print(line)
    print(row2)
    print(line)
    print(row3)
    print(line)
    print(row4)
    print(line)
    print(row5)
    print(line)
    print(row6)
    print(line)
    print(row7)
    print(line)
    print(row8)
    print(line)
    print('\n')

while True:
    print('\n'*10)
    print_board()
    make_move()
