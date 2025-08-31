# # Position structure (see readMe for details)
# solved_position = 'WWWWOOOGGGGRRRRBBBYYY'

# - - W W - - - - / - -  0  1  -  -  -  - 
# - - W W - - - - / - -  3  2  -  -  -  -
# O O G G R R B B / 4 5  7  8 11 12 15 16
# O O G G R R B B / - 6 10  9 14 13 17  -
# - - Y Y - - - - / - - 18 19 - - - -
# - - Y Y - - - - / - -  - 20 - - - -
def R(pos):
    
    return (pos[0] + pos[8] + pos[9] + pos[3] +
            pos[4] + pos[5] + pos[6] +
            pos[7] + pos[19] + pos[20] + pos[10] +
            pos[14] + pos[11] + pos[12] + pos[13] +
            pos[2] + pos[16] + pos[1] +
            pos[18] + pos[17] + pos[15])
def Rp(pos):
    return (pos[0]+pos[17]+pos[15]+pos[3]+
            pos[4]+pos[5]+pos[6]+
            pos[7]+pos[1]+pos[2]+pos[10]+
            pos[12]+pos[13]+pos[14]+pos[11]+
            pos[20]+pos[16]+pos[19]+
            pos[18]+pos[8]+pos[9])
def R2(pos):
    return (pos[0]+pos[19]+pos[20]+pos[3]+
            pos[4]+pos[5]+pos[6]+
            pos[7]+pos[17]+pos[15]+pos[10]+
            pos[13]+pos[14]+pos[11]+pos[12]+
            pos[9]+pos[16]+pos[8]+
            pos[18]+pos[1]+pos[2])

def F(pos):
    return (''+pos[0]+pos[1]+pos[5]+pos[6]+
            pos[4]+pos[18]+pos[19]+
            pos[10]+pos[7]+pos[8]+pos[9]+
            pos[3]+pos[12]+pos[13]+pos[2]+
            pos[15]+pos[16]+pos[17]+
            pos[14]+pos[11]+pos[20])

def Fp(pos):
    return (pos[0]+pos[1]+pos[14]+pos[11]+
            pos[4]+pos[2]+pos[3]+
            pos[8]+pos[9]+pos[10]+pos[7]+
            pos[19]+pos[12]+pos[13]+pos[18]+
            pos[15]+pos[16]+pos[17]+
            pos[5]+pos[6]+pos[20]) 
def F2(pos):
    return (pos[0]+pos[1]+pos[18]+pos[19]+
            pos[4]+pos[14]+pos[11]+
            pos[9]+pos[10]+pos[7]+pos[8]+
            pos[6]+pos[12]+pos[13]+pos[5]+
            pos[15]+pos[16]+pos[17]+
            pos[2]+pos[3]+pos[20])
def U(pos):
    return (pos[3]+pos[0]+pos[1]+pos[2]+
            pos[7]+pos[8]+pos[6]+
            pos[11]+pos[12]+pos[9]+pos[10]+
            pos[15]+pos[16]+pos[13]+pos[14]+
            pos[4]+pos[5]+pos[17]+
            pos[18]+pos[19]+pos[20])

def Up(pos):
    return (pos[1]+pos[2]+pos[3]+pos[0]+
            pos[15]+pos[16]+pos[6]+
            pos[4]+pos[5]+pos[9]+pos[10]+
            pos[7]+pos[8]+pos[13]+pos[14]+
            pos[11]+pos[12]+pos[17]+
            pos[18]+pos[19]+pos[20])
            
def U2(pos):
    return (pos[2]+pos[3]+pos[0]+pos[1]+
            pos[11]+pos[12]+pos[6]+
            pos[15]+pos[16]+pos[9]+pos[10]+
            pos[4]+pos[5]+pos[13]+pos[14]+
            pos[7]+pos[8]+pos[17]+
            pos[18]+pos[19]+pos[20])

