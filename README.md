# Mancala
Alpha-Beta Pruning and Minimax (Python) <br>

Python files:
<p> 1. MancalaGame.py = creates Mancala board, defines game moves, defines game rules </p>
<p> 2. MancalaGUI.py = creates visual of game board </p>
<p> 3. Player.py = creates different player options </p>

Player options: 
<p> HUMAN = human as the player </p>
<p> RANDOM = random legal moves </p>
<p> MINIMAX = uses minimax algorithm to choose next move</p>
<p> ABPRUNE = uses alpha-beta pruning algorithm to choose next move</p>
<p> NYG316 = most optimal player using ab-pruning </p>

To play:
<p>#define players (can choose any above player options)</p>
<p>>>>player1=Player(1, Player.HUMAN)</p>
<p>>>>player2=Player(2, Player.HUMAN)</p>
<p>>>>startGame(player1, player2)</p>
<p>#if you do not have another human to play against, choose one of the computer player options</p>

