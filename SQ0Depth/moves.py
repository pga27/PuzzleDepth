# Position Structure (see readMe for details)
solved_position = 'WWWWBBBBBRRRRRRGGGGGOOOOOOYYYY'

# - - W W - - - - / - -  0  1  -  -  -  - 
# - - W W - - - - / - -  3  2  -  -  -  -
# B B R R G G O O / 4 5  9 10 15 16 20 21
# B B R R G G O O / - 6 11 12 -  17 22 23
# B B R R G G O O / 7 8 13 14 18 19 24 25
# - - Y Y - - - - / - - 26 27 - - - -
# - - Y Y - - - - / - - 28 29 - - - - 

len(solved_position)

def Slash(state):
    return (state[0] + state[27] + state[29] + state[3] +
            state[4:9] + 
            state[9] + state[24] + state[11] + state[22] + state[13] + state[20] +
            state[19] + state[18] + state[17] + state[16] + state[15] +
            state[14] + state[21] + state[12] + state[23] + state[10] + state[25] +
            state[26] + state[1] + state[28] + state[2])

def D(state):
    return (state[0:4] +
            state[4:7] + state[24:26] + 
            state[9:13] + state[7:9] + 
            state[15:18] + state[13:15] +
            state[20:24] + state[18:20] + 
            state[28] + state[26] + state[29] + state[27])

def Dp(state):
    return (state[0:4] +
            state[4:7] + state[13:15] + 
            state[9:13] + state[18:20] + 
            state[15:18] + state[24:26] +
            state[20:24] + state[7:9] + 
            state[27] + state[29] + state[26] + state[28])

def D2(state):
    return (state[0:4] +
            state[4:7] + state[18:20] + 
            state[9:13] + state[24:26] + 
            state[15:18] + state[7:9] +
            state[20:24] + state[13:15] + 
            state[29] + state[28] + state[27] + state[26])

def U(state):
    return (state[3] + state[0:3] +
            state[9:11] + state[6:9] +
            state[15:17] + state[11:15] + 
            state[20:22] + state[17:20] +
            state[4:6] + state[22:26] + 
            state[26:])

def Up(state):
    return (state[1:4] + state [0] +
            state[20:22] + state[6:9] + 
            state[4:6] + state[11:15] + 
            state[9:11] + state[17:20] +
            state[15:17] + state[22:26] + 
            state[26:])

def U2(state):
    return (state[2:4] + state [0:2] +
            state[15:17] + state[6:9] + 
            state[20:22] + state[11:15] + 
            state[4:6] + state[17:20] +
            state[9:11] + state[22:26] + 
            state[26:])


