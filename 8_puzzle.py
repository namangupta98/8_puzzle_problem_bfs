import numpy as np
import random
import copy
import time

t = time.time()

# puzzle = np.array([[1, 0, 3], [4, 2, 5], [7, 8, 6]])
puzzle = np.arange(9)
np.random.shuffle(puzzle)
puzzle.shape = (3, 3)


def BlankTileLocation(p):
    for m in range(3):
        for n in range(3):
            if p[m, n] == 0:
                pos = m+1, n+1
    return pos


def ActionMoveLeft(puzL):
    m, n = BlankTileLocation(puzL)
    if n > 1:
        puzL[m-1, n-1] = puzL[m-1, n-1-1]
        puzL[m-1, n-1-1] = 0
        stat = 1
        # print(puzL, 'Inside function')
        # print('Moving left.')
    else:
        # print('Cannot move left.')
        stat = 0
    return stat, puzL


def ActionMoveRight(puzR):
    m, n = BlankTileLocation(puzR)
    if n < 3:
        puzR[m-1, n-1] = puzR[m-1, n-1+1]
        puzR[m-1, n-1+1] = 0
        stat = 1
        # print(puzR, 'Inside Function')
        # print('Moving right.')
    else:
        # print('Cannot move right!!')
        stat = 0
    return stat, puzR


def ActionMoveUp(puzU):
    m, n = BlankTileLocation(puzU)
    if m > 1:
        puzU[m-1, n-1] = puzU[m-1-1, n-1]
        puzU[m-1-1, n-1] = 0
        stat = 1
        # print(puzU, 'Inside Function')
        # print('Moving up.')
    else:
        # print('Cannot move up!!')
        stat = 0
    return stat, puzU


def ActionMoveDown(puzD):
    m, n = BlankTileLocation(puzD)
    if m < 3:
        puzD[m-1, n-1] = puzD[m-1+1, n-1]
        puzD[m-1+1, n-1] = 0
        stat = 1
        # print(puzD, 'Inside Function')
        # print('Moving down.')
    else:
        # print('Cannot move down!!')
        stat = 0
    return stat, puzD


def solvable(puzS):
    ctr = 0
    puzS = puzS.flatten()
    for m in range(9):
        for n in range(m+1, 9):
            if puzS[n] and puzS[m] and puzS[m] > puzS[n]:
                ctr += 1
    return ctr


def goalTest(puzG):
    goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    compare = puzG == goal
    return compare.all()


def explorer(puzE):
    queue = []
    puzzled = copy.deepcopy(puzE)
    # print(puzE, 'Parameter puzzle')
    # print(puzzled, 'Deep Copy puzzle')

    stat, puzzled = ActionMoveLeft(puzzled)
    # print(L_new_node, 'Returned puzzle Left')
    # tempL_new_node = copy.deepcopy(L_new_node)
    # print(tempL_new_node, 'Returned deep copy puzzle left')
    # print(puzE, 'Parameter puzzle')
    # print(puzzled, 'Deep Copy puzzle')
    if stat:
        # queue.append(tempL_new_node)
        queue.append(puzzled)
        # print(puzzled, 'Puzzled')
        # print(puzE, 'PuzE')

    puzzled = copy.deepcopy(puzE)
    # print(puzzled, 'Deep Copy puzzled')
    stat, puzzled = ActionMoveRight(puzzled)
    # print(R_new_node, 'Returned puzzle right')
    # tempR_new_node = copy.deepcopy(R_new_node)
    # print(tempR_new_node, 'Returned deep copy puzzle right')
    # print(puzE, 'Parameter puzzle')
    # print(puzzled, 'Deep Copy puzzle')
    if stat:
        # queue.append(tempR_new_node)
        queue.append(puzzled)
        # print(puzzled, 'Puzzled')
        # print(puzE, 'puzE')

    puzzled = copy.deepcopy(puzE)
    # print(puzzled, 'Deep copy puzzle')
    stat, puzzled = ActionMoveUp(puzzled)
    # print(U_new_node, 'Returned puzzle up')
    # tempU_new_node = copy.deepcopy(U_new_node)
    # print(tempU_new_node, 'Returned deep copy puzzle up')
    # print(puzE, 'Parameter puzzle')
    # print(puzzled, 'Deep Copy puzzle')
    if stat:
        # queue.append(tempU_new_node)
        queue.append(puzzled)
        # print(puzzled, 'Puzzled')
        # print(puzE, 'puzE')

    puzzled = copy.deepcopy(puzE)
    # print(puzzled, 'Deep copy puzzle')
    stat, puzzled = ActionMoveDown(puzzled)
    # print(D_new_node, 'Returned puzzle down')
    # tempD_new_node = copy.deepcopy(D_new_node)
    # print(tempD_new_node, 'Returned deep copy puzzle down')
    # print(puzE, 'Parameter puzzle')
    # print(puzzled, 'Deep Copy puzzle')
    if stat:
        # queue.append(tempD_new_node)
        queue.append(puzzled)
        # print(puzzled, 'Puzzled')
        # print(puzE, 'puzE')

    # print(queue, 'Queue')
    return queue


def bfs(p):
    frontier = [p]
    # frontier = explorer(p, frontier)
    explored = []
    iteration = -1

    while not len(frontier) == 0:
        iteration += 1
        print('Iteration: ', iteration)
        state = frontier.pop(0)
        explored.append(state)

        if goalTest(state):
            flg = 1
            return flg

        state_neighbors = explorer(state)
        # print(state_neighbors, 'State Neighbors')
        for neighbor in state_neighbors:
            galf = False
            for f in frontier:
                compare = neighbor == f
                if compare.all():
                    galf = True
                    break
            for e in explored:
                compare = neighbor == e
                if compare.all():
                    galf = True
                    break

            if not galf:
                frontier.append(neighbor)
                # print(frontier, 'Frontier')


# for i in range(3):
#     a = []
#     for j in range(3):
#         print('Enter ', i*3+j, 'th element: ')
#         a.append(int(input()))
#     p.append(a)
print(puzzle)
# if solvable(puzzle) % 2 is 0:
#     print('Solvable')
if solvable(puzzle) % 2 is 0:
    print('This is solvable')
    # i, j = BlankTileLocation(puzzle)
    # print('Blank space at row', i, 'and column', j)
    flag = bfs(puzzle)
    if flag:
        print('Success !!!!')
    else: print('Failure :(')

else:
    print('This is not solvable !!!')

old_t = t
t = time.time()
t_elapsed = t - old_t
print('Total Time Taken: ', t_elapsed)