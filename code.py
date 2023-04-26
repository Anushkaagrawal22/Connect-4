##############

#Your program can go here.



import numpy as np
import copy
import random
from math import *


##################################################
class Node:
    def __init__(self,state=None, move=None, parent=None ):
        self.state = state.Clone()
        self.parent = parent
        self.move = move
        self.moves = self.get_all_moves()
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.player = state.player
        

    def get_all_moves(self):
        #all the unvisited nodes are initialised to false
        all_moves = {}
        moves = self.state.getMoves()
        for move in moves:
            all_moves[move] = False

        return all_moves
        
    def selection(self,C):
        max = -inf
        selected = None
        
        for child in self.childNodes:
           val = child.wins/child.visits 
           val +=  sqrt((C * log(self.visits)) / child.visits)
           if(max<val):
               max = val
               selected = child

        return selected
        
    def expand(self, move, state):
        child = Node(move=move, parent=self, state=state)
        ### CHANGE
        self.moves[move] = True
        self.childNodes.append(child)
        
        return child

    def update(self, result):
        self.wins += result
        self.visits += 1

        
    def not_tried_child(self):
        for move in self.moves.values():
            if(not move):
                return False

        return True

    def tried_child(self):
        count = 0
        for move in self.moves.values():
            if(move):
                return True

        return False
        
def MCTS(currentState, itermax, currentNode=None,C=5):
    rootnode = Node(state=currentState)
    if currentNode is not None: rootnode = currentNode
    
    for i in range(itermax):
        node = rootnode
        state = currentState.Clone()

        while node.not_tried_child() and node.tried_child():
            node = node.selection(C)
            state.move(node.move)

       
        if not node.not_tried_child():
            m = -1
            for key in node.moves:
                if(not node.moves[key]):
                    m = key
                    break

            state.move(m)        
            node = node.expand(m, state)
        
        
        while state.getMoves():
            r = state.getMoves()
            state.move(r[random.randint(0,len(r)-1)])

            
        
        while node is not None:
            node.update(state.result(node.player))
            node = node.parent
        

    max = -inf
    selected = None
    for child in rootnode.childNodes:
           val = child.wins/child.visits
           if(max<val):
               max = val
               selected = child


    return rootnode, selected.move


class Connect4:
    def __init__(self, ROW, COLUMN):
        self.board = np.zeros((ROW, COLUMN), dtype=int)
        self.ROW = ROW 
        self.COLUMN = COLUMN
        self.player = 1 
        
    def Clone(self):
        clone = Connect4(self.ROW, self.COLUMN)
        clone.board = copy.deepcopy(self.board)
        clone.player = self.player
        return clone
        
    def move(self, col):
        row = 0
        while self.board[row][col] == 0:
            row += 1
            if(row==self.ROW):
                break

        row -= 1
        self.board[row][col] = self.player
        self.player = 1 if(self.player==2) else 2
    
    def result(self, player):
        if self.winner() == player: 
            return 0 
        elif self.winner() > 0: 
            return 1
        elif self.draw(): 
            return 0.5 
    
    def isValidMove(self, col): 
        return self.board[0][col] == 0
    
   
    def winner(self):
        #row
        s = ''
        for row in self.board:
            for i in row:
                s += str(i)
            if '1111' in s:
                return 1
            if '2222' in s:
                return 2
            s = ''

        
        s = ''
        for column in range(self.COLUMN):
            for row in range(self.ROW):
                s += str(self.board[row][column])
            if '1111' in s:
                return 1
            if '2222' in s:
                return 2
            s = ''
        
        
        s = ''
        for rs in range(self.ROW):
            row = rs
            column = 0
            while row >= 0 and column < self.COLUMN:
                s += str(self.board[row][column])
                row-=1
                column+=1
            if '1111' in s:
                return 1
            if '2222' in s:
                return 2
            s = ''
        
        s = ''
        for cs in range(1, self.COLUMN):
            row = self.ROW - 1
            column = cs
            while row >= 0 and column < self.COLUMN:
                s += str(self.board[row][column])
                row-=1
                column+=1
            if '1111' in s:
                return 1
            if '2222' in s:
                return 2
            s = ''
                
        
        s = ''
        for rs in range(self.ROW):
            row = rs
            column = 0
            while row < self.ROW and column < self.COLUMN:
                s += str(self.board[row][column])
                row+=1
                column+=1
            if '1111' in s:
                return 1
            if '2222' in s:
                return 2
            s = ''
        
        s = ''
        for cs in range(1, self.COLUMN):
            row = 0
            column = cs
            while row < self.ROW and column < self.COLUMN:
                s += str(self.board[row][column])
                row+=1
                column+=1
            if '1111' in s:
                return 1
            if '2222' in s:
                return 2
            s = ''

        return 0
    

    def print_board(self):
        for row in self.board:
            for data in row:
                print(data, end = "\t")
            print()
        print()

    
    
    def draw(self):
        return not self.getMoves() and not self.winner()
    
    def complete(self):  
        return self.winner() or not self.getMoves()
    
    
    def getMoves(self):
        moves = []
        if self.winner():
             return moves
       
        for col in range(self.COLUMN):
            if self.board[0][col] == 0: 
                moves.append(col)

        return moves


def MC200(board, currentNode,C):
    return MCTS(board, 200, currentNode,C)

def MC40(board, currentNode,C):
    return MCTS(board, 40, currentNode,C)

def begin_game(board, order=0,C=5):
    node = Node(state=board)
    while True: 
        if order == 0:
            print("Player 1(MCTS 200)")
            node, col = MC200(board, node,C)
            print('Action Selcted %s\n' % (col+1))
            print("Value of next state according to MC200 ", node.wins/node.visits)

        elif order == 1:
            print("Player 2(MCTS 40)")
            node, col = MC40(board, node,C)
            print('Action Selected %s\n' % (col+1))
            print("Value of next state according to MC40 ", node.wins/node.visits)
        board.move(col)
        board.print_board()
        node = goto_childNode(node, board, col)
        order ^=1
        if board.complete(): break
    if not board.draw(): print('%s won' % "MC 40" if (board.winner()==2) else "MC200")
    else: print('Draw')    
    
def goto_childNode(node, board, move):
    for childnode in node.childNodes:
        if childnode.move == move:
            return childnode
    return Node(state=board)



def chose_action():
    print("Press 1 for MC200 vs MC40")
    m = int(input())

    if(m==1):
        Row, Column = 6,5
        order = 0
        C= 4
        c4 = Connect4(Row,Column)
        c4.print_board()
        begin_game(c4,order,C)
    
chose_action()





def PrintGrid(positions):
    print('\n'.join(' '.join(str(x) for x in row) for row in positions))
    print()
