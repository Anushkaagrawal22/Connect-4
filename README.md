# Connect-4
In the turn-based game Connect 4, two players place coloured discs in a grid with seven columns and six rows. The specified column's lowest vacant row is where the discs will land. A player wins the game when their own four discs are lined up in a straight horizontal, vertical or diagonal line.


To determine the best course of action given the present state of the game, the programme employs the Monte Carlo Tree Search technique. Four steps make up the algorithm: selection, expansion, simulation, and backpropagation.

Selection: Based on the children's trust values, the algorithm selects the best node's child in this stage. The exploratory term and the exploitation term, which regulate the ratio of the respective procedures, make up the two words that make up the trust value.

Expansion: Based on the conceivable moves that might be made from the present node, this approach is used to determine all potential children of a node from that node.

Simulation: Used to predict a potential outcome of a random game based on the current game state. This estimate will be used to compare a node's performance or dependability to that of its siblings.

Backpropagation: Used to record the outcome of the simulation step in each node along the path of the simulation. At all levels of the game tree, this enables us to distinguish better nodes from their siblings.

Then, depending on the average win to simulation ratio of each child node, we return the best child of the main//root node, which stores the game's current state. This returns the best move that can be made at the present location.

Furthermore, it is crucial to ensure that wins do not have a very high ratio with draws when assigning the appropriate weights to wins, losses, and draws. In that model, the algorithm will attempt to win from any position, making it vulnerable to losing, while drawings were a very viable option. The Wins_score/Draw_score ratio must therefore be higher than 1 but extremely near to it.

Choice of exploratory constant(C): The best child of the main//root node, which records the game's current state, is then returned based on the average win to simulation ratio of each child node. The best move that can be made at the current location is returned by this.

Furthermore, when determining the right weights for wins, losses, and draws, it is essential to make sure that winners do not have a particularly high ratio with draws. Drawings were a very plausible choice since in that approach, the algorithm will try to win from any position, making it prone to losing. Therefore, the Wins_score/Draw_score ratio must be greater than 1 but very close to it.
