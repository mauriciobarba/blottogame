This is a genetic algorithm to find an optimal solution to an instance of a modified version of the game of [Blotto](https://en.wikipedia.org/wiki/Blotto_game). 

Here are the rules of the modified version: There are 10 castles, numbered 1, 2, 3,..., 10, and worth 1, 2, 3, ..., 10 points respectively. You have 100 soldiers, which you can allocate between the castles however you wish. Your opponent also (independently) does the same. The number of soldiers on each castle is then compared, and for each castle, whoever has the most soldiers on that castle wins its points (in the case of a tie, no one gets points). In a given match, castles are fought in order (starting with castle 1). If at any point a player wins 3 consecutive castles, that player is automatically awarded all remaining castles.
NUM_RANDOM = 100
NUM_EVOLVED = 100
ITERS = 10000

There is some interesting game theory behind this game but it would be infeasible to apply game theories to blottoes because they would take forever to run. The winning strategy of this game is a randomized one as opposed to a deterministic one. Moreover, the game is zero-sum, meaning that if both players play optimally, they will both each 0 dollars in expectation. 

The purpose of this algorithm is thus to see which assignments might have a higher associated probability in the optimal randomized solution.

The way this algorithm works is by initializing 300 randomly generated assignments of soldiers to castles. At each iteration, each assignment versus each other. The assignments 100 with the most wins remain in the competition. To follow the genetic algorithm analogy, these 100 winning assignments have "children" or assignments that are almost identical to their parents with the exception of some minute changes. 100 of the "children" of the winning assignments are inserted into the tournament now. We also insert 100 randomly generated assignments into the tournament. We perform 1000 iterations. Once it's done running, we analyze the best blottoes to gain some intuition about the optimal strategy. 
