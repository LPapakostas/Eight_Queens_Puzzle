'''
You have a chessboard and eight queen pieces to place on
it. The only requirement is thar none of the queens 
threatens any of the others.
'''
import random

def conflict(state,nextX):
#The <conflict> function is given the position of the
#queens so far and returns <True> if a position for the 
#next queen generates any new conflicts.

# <nextX> --> suggested horizontal position of next queen
# <nextY> --> suggested vertical position of next queen
    nextY = len(state)
    for i in range(nextY):
        if ( abs(state[i]-nextX) in (0,nextY-i) ):
        # The expression abs(state[i]+nextX) in (0,nextY-i) 
        # indicates if a queen is on the same horizontial
        # position (0) or equal to the vertical dinstance 
        # (diagonal)
            return True
    return False

def queens(num=8,state=()):
#<num> --> number of queens in total
#<state> --> tuple of positions for the previous queens
#example : state[0] == 1 means that the queen in 0th line placed in 7th column
    for pos in range(num):
        if not (conflict(state,pos)):
            if ( len(state) == num-1):
                yield (pos,)
            else:
                for result in queens(num,state+(pos,)):
                    yield (pos,) + result

def pretty_print(solution):
    def line(pos,length = len(solution)):
        return '. '*(pos) + 'X ' + '. ' * (length-pos-1)
    for sol in solution:
        print(line(sol))

solutions = list(queens())
pretty_print(random.choice(solutions))