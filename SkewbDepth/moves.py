'''
'WWWWOOOOOGGGGRRRRBBBBBYYYYY'

-- -- -- 00 -- 01 -- -- -- -- -- --
-- -- -- -- 02 -- -- -- -- -- -- --
-- -- -- 03 -- xx -- -- -- -- -- --
04 -- 05 09 -- xx xx -- 13 17 -- 18
-- 06 -- -- 10 -- -- 14 -- -- 19 --
07 -- 08 11 -- 12 15 -- 16 20 -- 21
-- -- -- 22 -- 23 -- -- -- -- -- --
-- -- -- -- 24 -- -- -- -- -- -- --
-- -- -- 25 -- 26 -- -- -- -- -- --

'''
# Clockwise B rotation
def B(pos):
    return (pos[16]+pos[1]+pos[2]+pos[3]+
            pos[20]+pos[5]+pos[19]+pos[21]+pos[18]+
            pos[9]+pos[10]+pos[0]+pos[12]+
            pos[13]+pos[14]+pos[15]+pos[11]+
            pos[17]+pos[26]+pos[24]+pos[22]+pos[25]+
            pos[4]+pos[23]+pos[6]+pos[7]+pos[8])

# Counterclockwise B rotation
def Bp(pos):
    return (pos[11]+pos[1]+pos[2]+pos[3]+
            pos[22]+pos[5]+pos[24]+pos[25]+pos[26]+
            pos[9]+pos[10]+pos[16]+pos[12]+
            pos[13]+pos[14]+pos[15]+pos[0]+
            pos[17]+pos[8]+pos[6]+pos[4]+pos[7]+
            pos[20]+pos[23]+pos[19]+pos[21]+pos[18])

# Clockwise R rotation
def R(pos):
    return (pos[0]+pos[12]+pos[2]+pos[3]+
            pos[4]+pos[5]+pos[6]+pos[1]+pos[8]+
            pos[9]+pos[10]+pos[11]+pos[7]+
            pos[23]+pos[24]+pos[25]+pos[26]+
            pos[15]+pos[18]+pos[14]+pos[16]+pos[13]+
            pos[22]+pos[21]+pos[19]+pos[17]+pos[20])

# Counterclockwise R rotation
def Rp(pos):
    return (pos[0]+pos[7]+pos[2]+pos[3]+
            pos[4]+pos[5]+pos[6]+pos[12]+pos[8]+
            pos[9]+pos[10]+pos[11]+pos[1]+
            pos[21]+pos[19]+pos[17]+pos[20]+
            pos[25]+pos[18]+pos[24]+pos[26]+pos[23]+
            pos[22]+pos[13]+pos[14]+pos[15]+pos[16])

# Clockwise L rotation
def L(pos):
    return (pos[0]+pos[1]+pos[2]+pos[21]+
            pos[4]+pos[25]+pos[24]+pos[23]+pos[22]+
            pos[7]+pos[6]+pos[8]+pos[5]+
            pos[13]+pos[14]+pos[3]+pos[16]+
            pos[17]+pos[18]+pos[19]+pos[20]+pos[15]+
            pos[11]+pos[9]+pos[10]+pos[12]+pos[26])

# Counterclockwise L rotation
def Lp(pos):
    return (pos[0]+pos[1]+pos[2]+pos[15]+
            pos[4]+pos[12]+pos[10]+pos[9]+pos[11]+
            pos[23]+pos[24]+pos[22]+pos[25]+
            pos[13]+pos[14]+pos[21]+pos[16]+
            pos[17]+pos[18]+pos[19]+pos[20]+pos[3]+
            pos[8]+pos[7]+pos[6]+pos[5]+pos[26])

# Clockwise U rotation
def U(pos):
    return (pos[18]+pos[21]+pos[19]+pos[17]+
            pos[0]+pos[1]+pos[2]+pos[3]+pos[8]+
            pos[13]+pos[10]+pos[11]+pos[12]+
            pos[25]+pos[14]+pos[15]+pos[16]+
            pos[7]+pos[4]+pos[6]+pos[20]+pos[5]+
            pos[22]+pos[23]+pos[24]+pos[9]+pos[26])

# Counterclockwise U rotation
def Up(pos):
    return (pos[4]+pos[5]+pos[6]+pos[7]+
            pos[18]+pos[21]+pos[19]+pos[17]+pos[8]+
            pos[25]+pos[10]+pos[11]+pos[12]+
            pos[9]+pos[14]+pos[15]+pos[16]+
            pos[3]+pos[0]+pos[2]+pos[20]+pos[1]+
            pos[22]+pos[23]+pos[24]+pos[13]+pos[26])