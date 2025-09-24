
# Virtual Cat

This is a CLI tamagotchi game called Virtual Cat. Upon starting the game a virtual cat is born and can be given a name. The cat is born with default stats for its hunger and its weight which can be changed throughout the game by using the options in the main menu.  The options in the game include:
    
    0. Exit Game
    1. Help
    2. Play
    3. Feed
    4. Show Stats

In order to be able to play with the pet its hunger has to have a value of 2 or above. Once it reaches a value of 4 it can no longer be fed - the cat is full. Every time the pet gets fed the weight goes up. It loses weight by playing.
## Screenshots

![Start](/screenshots/1.png?raw=true "Start")

![Choice 1](/screenshots/choice1.png?raw=true "Information")

![Choice 2](/screenshots/choice2-hungry.png?raw=true "Cannot Play")

![Choice 2](/screenshots/choice2-notHungry.png?raw=true "Playing")

![Choice 3](/screenshots/choice3.png?raw=true "Eating")

![Choice 3](/screenshots/full.png?raw=true "Full")

![Choice 4](/screenshots/choice4.png?raw=true "Show Stats")




## Installation

The project uses colorama, a Python module, in order to have different colors of the text in the terminal. Install this dependancy by running the command:

    pip install colorama