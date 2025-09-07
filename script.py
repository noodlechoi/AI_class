# 2022180039 최미나
import copy
import sys

class State:
    def __init__(self, board, goal, depth = 0):
        self.board = board
        self.depth = depth
        self.goal = goal

    def get_new_board(self, i1, i2, depth):
        new_board = copy.deepcopy(self.board[:])
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, depth)

    def expand(self, depth):
        result = []
        if depth > 5: return result  # 깊이가 5 이상이면 더 이상 확장을 하지 않는다.
        i = self.board.index(0)
        if not i in [6, 7, 8]:  # Down
            result.append(self.get_new_board(i, i + 3, depth))
        if not i in [2, 5, 8]:  # Right
            result.append(self.get_new_board(i, i + 1, depth))
        if not i in [0, 1, 2]:  # Up
            result.append(self.get_new_board(i, i - 3, depth))
        if not i in [0, 3, 6]:  # Left
            result.append(self.get_new_board(i, i - 1, depth))
        return result

    def __str__(self):
        return str(self.board[:3]) + "\n" + \
            str(self.board[3:6]) + "\n" + \
            str(self.board[6:]) + "\n" + \
            "-----------------"

    def __eq__(self, other):
        return  self.board == other.board

    def __ne__(self, other):
        return self.board != other.board

def BFS(state):
    open_queue = []
    open_queue.append(state)

    closed_queue = []
    depth = 0

    count = 1
    while len(open_queue) != 0:
        current = open_queue.pop(0) # open 리스트 앞에서 삭제
        print(count)
        count += 1
        print(current)
        if current.board == goal:
            print("탐색 성공")
            break

        depth = current.depth + 1
        closed_queue.append(current)

        if depth > 5:
            continue
        for state in current.expand(depth):
            if (state in closed_queue) or (state in open_queue):
                continue
            else:
                open_queue.append(state)


def DFS(state, limit_depth):
    open_stack = []
    open_stack.append(state)

    closed_queue = []
    depth = 0

    count = 1
    while len(open_stack) != 0:
        current = open_stack.pop(0) # open 리스트 앞에서 삭제
        print(count)
        count += 1
        print(current)
        if current.board == goal:
            print("탐색 성공")
            return True

        if current.depth > limit_depth:
            continue
        depth = current.depth + 1
        closed_queue.append(current)

        if depth > 5:
            continue
        for state in current.expand(depth):
            if (state in closed_queue) or (state in open_stack):
                continue
            else:
                open_stack.insert(0, state) # 앞에서 추가
    return False

def IDDFS(state):
    for depth in range(0, sys.maxsize):
        if DFS(state, depth):
            break



puzzle = [2, 8, 3,
          1, 6, 4,
          7, 0, 5]
goal = [1, 2, 3,
        8, 0, 4,
        7, 6, 5]

IDDFS(State(puzzle, goal))
print("2022180039 최미나\n")