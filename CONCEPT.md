# What is the game?

The game is about throwing dice and counting the values.
There are a set of rules on how one is allowed to count the values and store the points.
The player with the most points wins the match.
There are 5 dice to throw.
Dice can be thrown up to 3 times in a round.
Dice can be locked.


## The rules

- Count all 1's on the dice faces
- Count all 2's on the dice faces
- Count all 3's on the dice faces
- Count all 4's on the dice faces
- Count all 5's on the dice faces
- Count all 6's on the dice faces
- Bonus points if all counts amount to 63 or more: 35 points

- Chance: Count all values from all dices
- Dreierpasch: Min 3 equal dice, count all values on the dice
- Viererpasch: Min 4 equal dice, count all values on the dice
- Full House: 3 equal dice + 2 equal dice, 25 points
- Kleine Straße: 4 values in ascending order, 30 points
- Große Straße: 5 values in ascending order, 40 points
- Kniffel: 5 equal dice, 50 points

## Implementation

The output is going to be put onto console.
The console is therefore the view layer of the game.
The game needs to be a starting point, the controller.
Dice are individual objects in the game.
The player gets a scoreboard with an upper area and a lower area, where the corresponding rules need to be applied.
Rules are individual objects?
Rules are checked against the thrown dice and given to be selected by the player.
When a player selects a rule to apply, the rule will get thrown out of the selection for the player and the points will be applied to the scoreboard of that player.
When all rules are applied, i.e. the game ends, special rules for the bonus points need to be applied, before calculating the final sum.

