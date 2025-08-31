import moves
import time

solved_position = 'WWWWBBBBBRRRRRRGGGGGOOOOOOYYYY'

def get_moves(state):
    return [moves.D(state), moves.Dp(state), moves.D2(state),
            moves.U(state), moves.Up(state), moves.U2(state),
            moves.Slash(state)]

def solve(start):
    start_time = time.time()
    dist = [{start}, set(get_moves(start))]
    total = len(dist[0]) + len(dist[1])
    while dist[-1]:
        dist.append(set())
        for pos in dist[-2]:
            for sub_pos in get_moves(pos):
                if sub_pos not in dist[-2] and sub_pos not in dist[-3]:
                    dist[-1].add(sub_pos)
        total += len(dist[-1])
        print('Depth ' + str(len(dist) - 1) + ': ' + str(len(dist[-1])) + ' positions')
    print('SQ0 Depth is ' + str(len(dist) - 2) + ', solved in ' + str(round(time.time() - start_time, 2)) + ' seconds with ' + str(total) + ' positions!')

solve(solved_position)