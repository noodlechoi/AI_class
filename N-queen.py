import copy, sys, queue

class State:
    def __init__(self, board, size, score=0, depth=0):
        self.board = board
        self.depth = depth
        self.score = score
        self.size = size    # n

    def get_new_board(self, i, depth):
        new_board = copy.deepcopy(self.board[:])
        new_board[i] = 1
        return State(new_board,self.size, self.score, depth)

    def expand(self, depth):
        result = []

        arr_size = (self.size * (depth - 1))    # 깊이에 따라 행 위치 지정
        for i in range(self.size):
            result.append(self.get_new_board((i + arr_size), depth))

        return result

    def f(self):
        return self.h() + self.g()

    # 배치했을 때 충돌하는 개수
    def h(self):
        score = 0
        indices = [i for i, v in enumerate(self.board) if v == 1]
        row, col = [], []
        # row, col 계산
        for i in indices:
            if i == 0:
                row.append(0)
                col.append(0)
                continue
            row.append(i  // self.size)
            col.append(i  % self.size)
        # 같은 행/열에 있을 때(자기 자신 제외)
        for v in set(row):
            score += row.count(v) - 1
        for v in set(col):
            score += col.count(v) - 1

        return score

    def g(self):
        return self.depth

    def __str__(self):
        text = f"f(n)={self.f()} h(n)={self.h()} g(n)={self.g()}\n"
        for i in range(self.size):
            row = i * self.size
            text += str(self.board[row:row+self.size]) + "\n"
        "-----------------"
        return text

    def __eq__(self, other):
        return self.board == other.board

    def __ne__(self, other):
        return self.board != other.board

    def __lt__(self, other):
        return self.f() < other.f()

    def __gt__(self, other):
        return self.f() > other.f()

def Astar(state):
    open_queue = queue.PriorityQueue()
    open_queue.put(state)

    closed_queue = []
    depth = 0
    count = 0
    while not open_queue.empty():
        current = open_queue.get()
        count += 1
        print(count)
        print(current)
        if current.score == 0 and depth >= current.size:
            print("탐색 성공")
            break

        depth = current.depth + 1
        for state in current.expand(depth):
            if state not in closed_queue and state not in open_queue.queue:
                open_queue.put(state)
        closed_queue.append(current)
    else:
        print("탐색 실패")

n = input("queen 개수 입력: ")
n = int(n)
puzzle = []
for i in range(n*n):
    puzzle.append(0)    # 0이면 빈칸

Astar(State(puzzle, n))

