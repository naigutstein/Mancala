# File: MancalaGame.py
# Defines a game of Mancala

from random import *
from copy import *
from Player import *

# some constants
INFINITY = 1.0e400

class MancalaBoard:
    def __init__(self):
        """ Initilize a game board for the game of mancala"""
        self.reset()
        
    def reset(self):
        """ Reselt the mancala board for a new game"""
        self.NCUPS = 6       # Cups per side
        self.scoreCups = [0, 0]
        self.P1Cups = [4]*self.NCUPS
        self.P2Cups = [4]*self.NCUPS

    def __repr__(self):
        ret = "P L A Y E R  2\n"
        ret += "\t6\t5\t4\t3\t2\t1\n"
        ret += "------------------------------------------------------------\n"
        ret += str(self.scoreCups[1]) + "\t"
        for elem in range(len(self.P2Cups)-1, -1, -1):
            ret += str(self.P2Cups[elem]) + "\t"
        ret += "\n\t"
        for elem in self.P1Cups:
            ret += str(elem) + "\t"
        ret += str(self.scoreCups[0])
        ret += "\n------------------------------------------------------------"
        ret += "\n\t1\t2\t3\t4\t5\t6\n"
        ret += "P L A Y E R  1\n"        
        return ret
        
    def legalMove( self, player, cup ):
        """ Returns whether or not a given move is legal or not"""
        if player.num == 1:
            cups = self.P1Cups
        else:
            cups = self.P2Cups
        return cup > 0 and cup <= len(cups) and cups[cup-1] > 0

    def legalMoves( self, player ):
        """ Returns a list of legal moves for the given player """
        if player.num == 1:
            cups = self.P1Cups
        else:
            cups = self.P2Cups
        moves = []
        for m in range(len(cups)):
            if cups[m] != 0:
                moves += [m+1]
        return moves


    def makeMove( self, player, cup ):
        again = self.makeMoveHelp(player, cup)
        if self.gameOver():
            # clear out the cups
            for i in range(len(self.P1Cups)):
                self.scoreCups[0] += self.P1Cups[i]
                self.P1Cups[i] = 0
            for i in range(len(self.P2Cups)):
                self.scoreCups[1] += self.P2Cups[i]
                self.P2Cups[i] = 0
            return False
        else:
            return again
            
    def makeMoveHelp( self, player, cup ):
        """ Make a move for the given player.
            Returns True if the player gets another turn and False if not.
            Assumes a legal move"""
        if player.num == 1:
            cups = self.P1Cups
            oppCups = self.P2Cups
        else:
            cups = self.P2Cups
            oppCups = self.P1Cups
        initCups = cups
        nstones = cups[cup-1]  # Pick up the stones
        cups[cup-1] = 0        # Now the cup is empty
        cup += 1
        playAgain = False # bug fix 
        while nstones > 0:
            playAgain = False    
            while cup <= len(cups) and nstones > 0:
                cups[cup-1] += 1
                nstones = nstones - 1
                cup += 1
            if nstones == 0:
                break    # If no more stones, exit the loop
            if cups == initCups:   # If we're on our own side
                self.scoreCups[player.num-1] += 1
                nstones = nstones - 1
                playAgain = True
            # now switch sides and keep going
            tempCups = cups
            cups = oppCups
            oppCups = tempCups
            cup = 1

        # If playAgain is True, then we landed in our Mancala, so this
        # play is over but we get to go again
        if playAgain:
            return True
        
        # Now see if we ended in a blank space on our side
        if cups == initCups and cups[cup-2] == 1:
            self.scoreCups[player.num-1] += oppCups[(self.NCUPS-cup)+1]
            oppCups[(self.NCUPS-cup)+1] = 0
            #added 2 lines so that when lands on own open cup, captures
            # opposite stones in addition to my own 1
            self.scoreCups[player.num-1] += 1
            cups[cup-2] = 0
        return False

    def hasWon( self, playerNum ):
        """ Returns whether or not the given player has won """
        if self.gameOver():
            opp = 2 - playerNum + 1
            return self.scoreCups[playerNum-1] > self.scoreCups[opp-1]
        else:
            return False

    def getPlayersCups( self, playerNum ):
        """ Return the cups for the given player """
        if playerNum == 1:
            return self.P1Cups
        else:
            return self.P2Cups
        
    def gameOver(self):
        """ Is the game over?"""
        over = True
        for elem in self.P1Cups:
            if elem != 0:
                over = False
        if over:
            return True
        over = True
        for elem in self.P2Cups:
            if elem != 0:
                over = False
        return over   

    def hostGame(self, player1, player2):
        """ Host a game between two players """
        self.reset()
        currPlayer = player1 
        waitPlayer = player2
        while not(self.gameOver()):
            again = True
            while again:
                print self
                move = currPlayer.chooseMove( self )
                while not(self.legalMove(currPlayer, move)):
                    print move, " is not legal"
                    move = currPlayer.chooseMove(self)
                again = self.makeMove( currPlayer, move )
            temp = currPlayer
            currPlayer = waitPlayer
            waitPlayer = temp

        print self
        if self.hasWon(currPlayer.num):
            print "Player", currPlayer, " wins!"
        elif self.hasWon(waitPlayer.num):
            print "Player", waitPlayer, " wins!"
        else:
            print "Tie Game"
