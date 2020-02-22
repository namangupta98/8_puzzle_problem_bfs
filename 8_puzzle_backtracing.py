import numpy as np
import random
import copy
import time

t = time.time()  # Stopwatch started
puzzle = []  # Created an empty list
# puzzle = np.array([[1, 0, 3], [4, 2, 5], [7, 8, 6]])
# puzzle = np.arange(9)
# np.random.shuffle(puzzle)
# puzzle.shape = (3, 3)

# Created class for back tracing the path
class Tree:
    def __init__(self, child, parent=None, index=0):
        self.child = child
        self.parent = parent
        self.index = index

# function to find blank tile's location
def BlankTileLocation(p):
    for m in range(3):
        for n in range(3):
            if p[m, n] == 0:
                pos = m+1, n+1
    return pos

# function to backtrace the path
def backtrace(strate):
    street = []
    current_state = strate
    while current_state is not None:
        street.append(current_state)
        current_state = current_state.parent
    street.reverse()

    # Create a empty file
    with open('nodePath.txt', 'w') as nPath:
        for current_state in street:
            # Writing path in the text file
            nPath.writelines(str(current_state.child.flatten('F')).strip('[]')+'\n')

# function to move the blank tile left
def ActionMoveLeft(puzL):
    #m, n = BlankTileLocation(puzL)
    m, n = BlankTileLocation(puzL.child)
    if n > 1:
        puzL.child[m-1, n-1] = puzL.child[m-1, n-1-1]
        puzL.child[m-1, n-1-1] = 0
        stat = 1
        # print(puzL, 'Inside function')
        # print('Moving left.')
    else:
        # print('Cannot move left.')
        stat = 0
    return stat, puzL

# function to move the blank tile right
def ActionMoveRight(puzR):
    m, n = BlankTileLocation(puzR.child)
    if n < 3:
        puzR.child[m-1, n-1] = puzR.child[m-1, n-1+1]
        puzR.child[m-1, n-1+1] = 0
        stat = 1
        # print(puzR, 'Inside Function')
        # print('Moving right.')
    else:
        # print('Cannot move right!!')
        stat = 0
    return stat, puzR

# function to move the blank tile up
def ActionMoveUp(puzU):
    m, n = BlankTileLocation(puzU.child)
    if m > 1:
        puzU.child[m-1, n-1] = puzU.child[m-1-1, n-1]
        puzU.child[m-1-1, n-1] = 0
        stat = 1
        # print(puzU, 'Inside Function')
        # print('Moving up.')
    else:
        # print('Cannot move up!!')
        stat = 0
    return stat, puzU

# function to move the blank tile down
def ActionMoveDown(puzD):
    m, n = BlankTileLocation(puzD.child)
    if m < 3:
        puzD.child[m-1, n-1] = puzD.child[m-1+1, n-1]
        puzD.child[m-1+1, n-1] = 0
        stat = 1
        # print(puzD, 'Inside Function')
        # print('Moving down.')
    else:
        # print('Cannot move down!!')
        stat = 0
    return stat, puzD

# function to check the solvability of the puzzle
def solvable(puzS):
    ctr = 0
    puzS = puzS.flatten()
    for m in range(9):
        for n in range(m+1, 9):
            if puzS[n] and puzS[m] and puzS[m] > puzS[n]:
                ctr += 1
    return ctr

# function to check goal achieved or not
def goalTest(puzG):
    goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    compare = puzG.child == goal
    return compare.all()

# function to explore tree
def explorer(puzE):
    queue = []
    puzzled = copy.deepcopy(puzE)
    puzzled.parent = puzE
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
        puzzled.index = puzE.index + 1
        # print(puzzled, 'Puzzled')
        # print(puzE, 'PuzE')

    puzzled = copy.deepcopy(puzE)
    puzzled.parent = puzE
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
        puzzled.index = puzE.index + 2
        # print(puzzled, 'Puzzled')
        # print(puzE, 'puzE')

    puzzled = copy.deepcopy(puzE)
    puzzled.parent = puzE
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
        puzzled.index = puzE.index + 3
        # print(puzzled, 'Puzzled')
        # print(puzE, 'puzE')

    puzzled = copy.deepcopy(puzE)
    puzzled.parent = puzE
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
        puzzled.index = puzE.index + 4
        # print(puzzled, 'Puzzled')
        # print(puzE, 'puzE')

    # print(queue, 'Queue')
    return queue

# function to implement Breadth First Search
def bfs(p):
    # parent = {}
    frontier = [p]
    # frontier = explorer(p, frontier)
    explored = []
    iteration = -1

    rf = open('NodesInfo.txt', 'w')

    while not len(frontier) == 0:
        iteration += 1
        print('Iteration: ', iteration)
        state = frontier.pop(0)
        explored.append(state.child)

        # condition for no parent
        try:
            rf.writelines(str(iteration+1) + ' ' + str(state.index) + ' ' + str(state.parent.index)+'\n')
        except:
            rf.writelines(str(iteration + 1) + ' ' + str(state.index) + ' ' + str(state.index)+'\n')

        # check goal reached or not
        if goalTest(state):
            flg = 1
            backtrace(state)
            return flg, explored, iteration

        state_neighbors = explorer(state)
        # print(state_neighbors, 'State Neighbors')
        for neighbor in state_neighbors:
            galf = False
            for f in frontier:
                compare = neighbor.child == f
                if compare.all():
                    galf = True
                    break
            for e in explored:
                compare = neighbor.child == e
                if compare.all():
                    galf = True
                    break

            if not galf:
                frontier.append(neighbor)
                # print(frontier, 'Frontier')
    rf.close()


for i in range(3):
    a = []
    for j in range(3):
        print('Enter ', i*3+j, 'th element in row order: ')
        a.append(int(input()))
    puzzle.append(a)

puzzle = np.asarray(puzzle)
print(puzzle)
# if solvable(puzzle) % 2 is 0:
#     print('Solvable')

# Object of class Tree
start = Tree(puzzle)

if solvable(puzzle) % 2 is 0:
    print('This is solvable')
    # i, j = BlankTileLocation(puzzle)
    # print('Blank space at row', i, 'and column', j)
    flag, exp, iterat = bfs(start)
    if flag:
        print('Success !!!!')
    else:
        print('Failure :(')

else:
    print('This is not solvable !!!')

nodes = open('Nodes.txt','w')
# exp = np.array(exp)
for i in range(iterat+1):
    exp[i] = exp[i].flatten(order='F')
    nodes.writelines(str(exp[i]).strip('[]')+'\n')

nodes.close()   # close the file

old_t = t
t = time.time()
t_elapsed = t - old_t   # Total Time
print('Total Time Taken: ', t_elapsed, 'ms')
