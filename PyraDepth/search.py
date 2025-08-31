import moves
import time

# Position structure (see readMe for details)


# Takes a position and returns a list of all the positions that arise from performing every move
def get_moves(pos):
	return [moves.L(pos), moves.Lp(pos), moves.B(pos),moves.R(pos), moves.Rp(pos), moves.Bp(pos),moves.U(pos), moves.Up(pos), 
			moves.l(pos), moves.lp(pos), moves.b(pos),moves.r(pos), moves.rp(pos), moves.bp(pos),moves.u(pos), moves.up(pos),]

# Solves the problem
def solve():
	solved_position = 'RRRRRRRRRGGGGGGGGGBBBBBBBBBYYYYYYYYY'
	start_time = time.time()
	total = 0
	dist = [{solved_position}, set(get_moves(solved_position))]
	while dist[-1]:
		dist.append(set())
		for pos in dist[-2]:
			for sub_pos in get_moves(pos):
				if sub_pos not in dist[-2] and sub_pos not in dist[-3]:
					dist[-1].add(sub_pos)
		total += len(dist[-1])
		print('Depth ' + str(len(dist) - 1) + ': ' + str(len(dist[-1])) + ' positions')
	print('Pyraminx Depth is ' + str(len(dist) - 2) + ', solved in ' + str(round(time.time() - start_time, 2)) + ' seconds with ' + str(total) + ' positions!')

solve()