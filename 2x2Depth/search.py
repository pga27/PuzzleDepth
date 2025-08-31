import moves
import time

# Position structure (see readMe for details)
solved_position = 'WWWWOOOGGGGRRRRBBBYYY'

# Takes a position and returns a list of all the positions that arise from performing every move
def get_moves(pos):
	return [moves.F(pos), moves.Fp(pos), moves.F2(pos),
			moves.R(pos), moves.Rp(pos), moves.R2(pos),
			moves.U(pos), moves.Up(pos), moves.U2(pos)]

# Solves the problem
def solve():
	solved_position = 'WWWWOOOGGGGRRRRBBBYYY'
	start_time = time.time()
	dist = [{solved_position}, set(get_moves(solved_position))]
	total = len(dist[0]) + len(dist[1])
	while dist[-1]:
		dist.append(set())
		for pos in dist[-2]:
			for sub_pos in get_moves(pos):
				if sub_pos not in dist[-2] and sub_pos not in dist[-3]:
					dist[-1].add(sub_pos)
		total += len(dist[-1])
		print('Depth ' + str(len(dist) - 1) + ': ' + str(len(dist[-1])) + ' positions')
	print('2x2 Depth is ' + str(len(dist) - 2) + ', solved in ' + str(round(time.time() - start_time, 2)) + ' seconds with ' + str(total) + ' positions!')

solve()