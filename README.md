# Ping Pong Game Project

## Game Objective
The Ping Pong game is a two-player game where each player controls a paddle to hit a ball back and forth across the screen. The objective is to prevent the ball from passing your paddle and to score points by getting the ball past the opponent's paddle.

## Implementation
The game is developed using the Python programming language and the `pygame` library, which is utilized for rendering graphics, handling game logic, and managing user input.

## Gameplay Mechanics
- **Controls**: Each player controls their paddle using specific keys. Typically, one player uses the `W` and `S` keys for up and down movements, while the other uses the `Up` and `Down` arrow keys.
- **Ball Movement**: The ball starts moving in a random direction and bounces off the top and bottom edges of the screen. Players use their paddles to hit the ball back to the opponent.
- **Scoring**: A point is scored when a player fails to return the ball, allowing it to pass by their paddle. The game keeps track of each player's score.

## End Condition
The game continues until one of the players reaches a predefined winning score. At that point, the game displays the winner and offers an option to restart the game.
