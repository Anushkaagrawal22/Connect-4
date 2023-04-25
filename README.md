# Connect-4
Connect 4 is a turn based game, where 2 players drop colored disks in a grid with 7 columns and 6 rows. The disks drop to the lowest empty row in the chosen column. A players wins the game when a consecutive horizontal, vertical or diagonal line of own 4 disks is formed.

The algorithm uses the Monte Carlo Tree Search method to find the most optimal move from the current game state. The algorithm consists of four steps, namely: selection, expansion, simulation, backpropagation.

Selection: In this step, the algorithm chooses the best possible child of a node based on the trust value of the children. The trust value consists of two terms: exploratory term and exploitation term which control the ratio of respective methods.

Expansion: This method is used to find all possible children of a node from a current given node, based on the possible moves that can be played from that node.

Simulation: Used to estimate a possible result of an arbitrary game played from the given state of the game. This estimate will be used to find how good or reliable a node is, as compared to its sibling nodes.

Backpropagation: Used to store the result, obtained in the simulation step, in all nodes occurring in the simulation path. This helps us differentiate better nodes from the sibling nodes at all levels of the game tree.

Finally we return the best child of the main//root node, which stores the current state of the game, therefore returning the best possible move at the current position, based on the average win to simulation ratio of each child node.

Additionally, while giving the respective weightage to wins, losses and draws, it is important that win does not have a very high ratio with draw, because in that model, algorithm will try to win from any state making it vulnerable to losing, while draw was a very possible solution. So, it is important that the ratio of Wins_score/Draw_score is higher than 1 but very close to it.

Choice of exploratory constant(C): The choice of C, depending on the number of simulations, has an impact on the results achieved.As the number of simulations increases, more iterations are available to explore more possible moves and thus higher value of C should be preferred with increasing simulations. Therefore a higher value of C prefers the MC200 algorithm to give better results than MC40, whereas a lower value of C prefers MC40 to exploit better moves thus giving precise results in respective cases. This relation is also visible in the small sample of data tabulated above, where as C decreases the performance of MC40 improves, whereas when C increases the performance of MC200 gets better.
