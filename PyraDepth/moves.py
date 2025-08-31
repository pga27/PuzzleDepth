'''
Excluding tips, increases the total number of positions by a factor of 3^4(81)


-- -- 00 -- -- -- -- 09 -- -- -- -- 18 -- --
-- 01 02 03 -- -- 10 11 12 -- -- 19 20 21 -- 
04 05 06 07 08 13 14 15 16 17 22 23 24 25 26
-- -- -- -- -- 27 28 29 30 31 -- -- -- -- --
-- -- -- -- -- -- 32 33 34 -- -- -- -- -- --
-- -- -- -- -- -- -- 35 -- -- -- -- -- -- --

'''
# Clockwise B rotation
def B(pos):
    return (pos[0]+pos[24]+pos[2]+pos[3]+pos[26]+pos[25]+pos[21]+pos[7]+pos[8]+
            pos[9]+pos[10]+pos[11]+pos[12]+pos[13]+pos[14]+pos[15]+pos[16]+pos[17]+
            pos[18]+pos[19]+pos[20]+pos[34]+pos[22]+pos[23]+pos[32]+pos[33]+pos[35]+
            pos[27]+pos[28]+pos[29]+pos[30]+pos[31]+pos[1]+pos[5]+pos[6]+pos[4])

# Counterclockwise B rotation
def Bp(pos):
    return (pos[0]+pos[32]+pos[2]+pos[3]+pos[35]+pos[33]+pos[34]+pos[7]+pos[8]+
            pos[9]+pos[10]+pos[11]+pos[12]+pos[13]+pos[14]+pos[15]+pos[16]+pos[17]+
            pos[18]+pos[19]+pos[20]+pos[6]+pos[22]+pos[23]+pos[1]+pos[5]+pos[4]+
            pos[27]+pos[28]+pos[29]+pos[30]+pos[31]+pos[24]+pos[25]+pos[21]+pos[26])

# Clockwise Tip B rotation
def b(pos):
    return (pos[0]+pos[1]+pos[2]+pos[3]+pos[26]+pos[5]+pos[6]+pos[7]+pos[8]+
            pos[9]+pos[10]+pos[11]+pos[12]+pos[13]+pos[14]+pos[15]+pos[16]+pos[17]+
            pos[18]+pos[19]+pos[20]+pos[21]+pos[22]+pos[23]+pos[24]+pos[25]+pos[35]+
            pos[27]+pos[28]+pos[29]+pos[30]+pos[31]+pos[32]+pos[33]+pos[34]+pos[4])

# Counterclockwise Tip B rotation
def bp(pos):
    return (pos[0]+pos[1]+pos[2]+pos[3]+pos[35]+pos[5]+pos[6]+pos[7]+pos[8]+
            pos[9]+pos[10]+pos[11]+pos[12]+pos[13]+pos[14]+pos[15]+pos[16]+pos[17]+
            pos[18]+pos[19]+pos[20]+pos[21]+pos[22]+pos[23]+pos[24]+pos[25]+pos[4]+
            pos[27]+pos[28]+pos[29]+pos[30]+pos[31]+pos[32]+pos[33]+pos[34]+pos[26])

# Clockwise u rotation
def u(pos):
    return (pos[9]+pos[1]+pos[2]+pos[3]+pos[4]+pos[5]+pos[6]+pos[7]+pos[8]+
            pos[18]+pos[10]+pos[11]+pos[12]+pos[13]+pos[14]+pos[15]+pos[16]+pos[17]+
            pos[0]+pos[19]+pos[20]+pos[21]+pos[22]+pos[23]+pos[24]+pos[25]+pos[26]+
            pos[27]+pos[28]+pos[29]+pos[30]+pos[31]+pos[32]+pos[33]+pos[34]+pos[35])

# Counterclockwise u rotation
def up(pos):
    return (pos[18]+pos[1]+pos[2]+pos[3]+pos[4]+pos[5]+pos[6]+pos[7]+pos[8]+
            pos[0]+pos[10]+pos[11]+pos[12]+pos[13]+pos[14]+pos[15]+pos[16]+pos[17]+
            pos[9]+pos[19]+pos[20]+pos[21]+pos[22]+pos[23]+pos[24]+pos[25]+pos[26]+
            pos[27]+pos[28]+pos[29]+pos[30]+pos[31]+pos[32]+pos[33]+pos[34]+pos[35])

# Clockwise l rotation
def l(pos):
    return (pos[0]+pos[1]+pos[2]+pos[3]+pos[4]+pos[5]+pos[6]+pos[7]+pos[27]+
            pos[9]+pos[10]+pos[11]+pos[12]+pos[8]+pos[14]+pos[15]+pos[16]+pos[17]+
            pos[18]+pos[19]+pos[20]+pos[21]+pos[22]+pos[23]+pos[24]+pos[25]+pos[26]+
            pos[13]+pos[28]+pos[29]+pos[30]+pos[31]+pos[32]+pos[33]+pos[34]+pos[35])

# Counterclockwise l rotation
def lp(pos):
    return (pos[0]+pos[1]+pos[2]+pos[3]+pos[4]+pos[5]+pos[6]+pos[7]+pos[13]+
            pos[9]+pos[10]+pos[11]+pos[12]+pos[27]+pos[14]+pos[15]+pos[16]+pos[17]+
            pos[18]+pos[19]+pos[20]+pos[21]+pos[22]+pos[23]+pos[24]+pos[25]+pos[26]+
            pos[8]+pos[28]+pos[29]+pos[30]+pos[31]+pos[32]+pos[33]+pos[34]+pos[35])

# Clockwise r rotation
def r(pos):
    return (pos[0]+pos[1]+pos[2]+pos[3]+pos[4]+pos[5]+pos[6]+pos[7]+pos[8]+
            pos[9]+pos[10]+pos[11]+pos[12]+pos[13]+pos[14]+pos[15]+pos[16]+pos[31]+
            pos[18]+pos[19]+pos[20]+pos[21]+pos[17]+pos[23]+pos[24]+pos[25]+pos[26]+
            pos[27]+pos[28]+pos[29]+pos[30]+pos[22]+pos[32]+pos[33]+pos[34]+pos[35])

# Counterclockwise r rotation
def rp(pos):
    return (pos[0]+pos[1]+pos[2]+pos[3]+pos[4]+pos[5]+pos[6]+pos[7]+pos[8]+
            pos[9]+pos[10]+pos[11]+pos[12]+pos[13]+pos[14]+pos[15]+pos[16]+pos[22]+
            pos[18]+pos[19]+pos[20]+pos[21]+pos[31]+pos[23]+pos[24]+pos[25]+pos[26]+
            pos[27]+pos[28]+pos[29]+pos[30]+pos[17]+pos[32]+pos[33]+pos[34]+pos[35])

# Clockwise U rotation
def U(pos):
    return (pos[9]+pos[10]+pos[11]+pos[12]+pos[4]+pos[5]+pos[6]+pos[7]+pos[8]+
            pos[18]+pos[19]+pos[20]+pos[21]+pos[13]+pos[14]+pos[15]+pos[16]+pos[17]+
            pos[0]+pos[1]+pos[2]+pos[3]+pos[22]+pos[23]+pos[24]+pos[25]+pos[26]+
            pos[27]+pos[28]+pos[29]+pos[30]+pos[31]+pos[32]+pos[33]+pos[34]+pos[35])

# Counterclockwise U rotation
def Up(pos):
    return (pos[18]+pos[19]+pos[20]+pos[21]+pos[4]+pos[5]+pos[6]+pos[7]+pos[8]+
            pos[0]+pos[1]+pos[2]+pos[3]+pos[13]+pos[14]+pos[15]+pos[16]+pos[17]+
            pos[9]+pos[10]+pos[11]+pos[12]+pos[22]+pos[23]+pos[24]+pos[25]+pos[26]+
            pos[27]+pos[28]+pos[29]+pos[30]+pos[31]+pos[32]+pos[33]+pos[34]+pos[35])

# Clockwise L rotation
def L(pos):
    return (pos[0]+pos[1]+pos[2]+pos[32]+pos[4]+pos[5]+pos[29]+pos[28]+pos[27]+
            pos[9]+pos[6]+pos[11]+pos[12]+pos[8]+pos[7]+pos[3]+pos[16]+pos[17]+
            pos[18]+pos[19]+pos[20]+pos[21]+pos[22]+pos[23]+pos[24]+pos[25]+pos[26]+
            pos[13]+pos[14]+pos[10]+pos[30]+pos[31]+pos[15]+pos[33]+pos[34]+pos[35])

# Counterclockwise L rotation
def Lp(pos):
    return (pos[0]+pos[1]+pos[2]+pos[15]+pos[4]+pos[5]+pos[10]+pos[14]+pos[13]+
            pos[9]+pos[29]+pos[11]+pos[12]+pos[27]+pos[28]+pos[32]+pos[16]+pos[17]+
            pos[18]+pos[19]+pos[20]+pos[21]+pos[22]+pos[23]+pos[24]+pos[25]+pos[26]+
            pos[8]+pos[7]+pos[6]+pos[30]+pos[31]+pos[3]+pos[33]+pos[34]+pos[35])

# Clockwise R rotation
def R(pos):
    return (pos[0]+pos[1]+pos[2]+pos[3]+pos[4]+pos[5]+pos[6]+pos[7]+pos[8]+
            pos[9]+pos[10]+pos[11]+pos[29]+pos[13]+pos[14]+pos[34]+pos[30]+pos[31]+
            pos[18]+pos[15]+pos[20]+pos[21]+pos[17]+pos[16]+pos[12]+pos[25]+pos[26]+
            pos[27]+pos[28]+pos[24]+pos[23]+pos[22]+pos[32]+pos[33]+pos[19]+pos[35])

# Counterclockwise R rotation
def Rp(pos):
    return (pos[0]+pos[1]+pos[2]+pos[3]+pos[4]+pos[5]+pos[6]+pos[7]+pos[8]+
            pos[9]+pos[10]+pos[11]+pos[24]+pos[13]+pos[14]+pos[19]+pos[23]+pos[22]+
            pos[18]+pos[34]+pos[20]+pos[21]+pos[31]+pos[30]+pos[29]+pos[25]+pos[26]+
            pos[27]+pos[28]+pos[12]+pos[16]+pos[17]+pos[32]+pos[33]+pos[15]+pos[35])