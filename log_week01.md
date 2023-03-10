# 100 Days Of Code - Week 1
### [Link to Week 1 Files](https://github.com/hrbird/100-days-of-code-2023/tree/master/week01)

-----

## Day 7. Python Enums, HTML Links and Videos
### January 18, 2023

**Today's Progress**: 
- Continued working through "100 Days of Python" Udemy class. Completed day 17.
- Focused on object-oriented programming and enums in Python. Also, using links, images, and videos in HTML.

**Programs**:
- **dice_roller.py**: This program simulates rolling dice for table-top roleplaying games, like DND or Pathfinder. It can roll dice with 4, 6, 8, 10, 12, 20, or 100 sides.<br />
  ![img](/screenshots/007_dice.jpg)
- **ducklings.py**: This program creates a randomized field of ASCII ducklings. First, it prints a row of 10 ducklings. Then, it prints a scrolling screen filled with random ducklings.<br />
  ![img](/screenshots/007_ducklings.jpg)
- **install-extension.html**: Added navigation links, images, and a video to the install-extension page.

**Thoughts:** Still enjoying learning new things with every project! For this first week, I organized my files into daily folders, since I made several small programs per day. However, next week I think I will put all of the one-file programs into a "small_python_projects" folder and put larger projects into their own subfolders. This will make it easier to work on more complex programs that may take 2+ days to complete.

-----

## Day 6. Object-Oriented Programming in Python, VSCode Live Server
### January 17, 2023

**Today's Progress**: 
- Continued working through "100 Days of Python" Udemy class. Completed day 16 and part of day 17.
- Focused on object-oriented programming in Python. Also reviewed some basic HTML, and how to use VSCode Live Server to easily preview HTML pages.

**Programs**:
- **install-extension.html**: Simple HTML file to learn the basic HTML structure and elements.
- **coffee_machine/main.py**: Tidied up the Coffee Machine project from yesterday by creating a new CoffeeMachine class to encapsulate all of the related objects and code for the coffee machine. This cleans up the main function of the program so it only needs to create a CoffeeMachine object and call its start_machine function. It loops while the machine is on, so multiple drinks can be ordered in a row.

**Quiz Project**:
- **main.py**: Main program
- **data.py**: A list of objects containing data for each question: the question text and the answer (True or False)
- **question**: The Question class, which models each quiz question.
- **quiz_brain.py**: The QuizBrain class, which manages the quiz. It asks the user the questions, validates that each answer is T or F, checks if the answers are right, checks if they reached the end of the quiz, and calculates the final score.<br />
  ![img](/screenshots/006_quiz_1.jpg) [Snipped...] ![img](/screenshots/006_quiz_2.jpg)

**Thoughts:** Feeling more confident with creating and using Python classes.

-----

## Day 5. Coffee Machine Project
### January 16, 2023

**Today's Progress**: 
- Continued working through "100 Days of Python" Udemy class. Continued working on day 16.
- Focused on object-oriented programming in Python, PyPi, and learning how to install other python packages. Also a little HTML.

**Coffee machine project**:
- **main.py**: This program pretends to be a coffee machine that can make a list of drinks, process coins and return change, and check current levels of resources (water, milk, coffee grounds).
- **coffee_maker.py**: CoffeeMaker class that makes the coffee and manages the current levels of resources. If there aren't enough resources left to make the ordered drink, the drink is not made and the user is told why.
- **menu.py**: MenuItem class that handles the name, cost, and amounts of resources (water, milk, coffee grounds) used by each of the coffee machine drinks. Menu class that manages all of the MenuItem objects.
- **money_machine.py**: MoneyMachine class that processes coins, accepts or refuses payments, and calculates change. If the user does not enter enough money after ordering a drink, the drink is not made and their money is returned to them.<br />
- **screenshots**: 
  - Ordering a drink:<br />
    ![img](/screenshots/005_coffee.jpg)<br />
  - Checking resource levels (secret code 0):<br />
    ![img](/screenshots/005_coffee_2.jpg)<br />

**Thoughts:** I started the OOP Coffee Maker project and feel like I'm getting the hang of how to use python classes.

-----

## Day 4. Turtle Graphics Library
### January 15, 2023

**Today's Progress**: 
- I started this 100-days project on Jan 12 in a fork of the repository made by the original creator of this challenge. However, I have just learned that GitHub does not count commits in forked repositories as contributions in your user profile. Therefore, I am copying my work from the first 3 days into a new, standalone repository!
- Continued working through "100 Days of Python" Udemy class. Completed days 12-15 and half of day 16.
- Focused on variable scope, object-oriented programming, and the turtle graphics library.

**Programs**:
- **learn_turtle.py**: Simple program that creates a green turtle and has it create an original modern art piece by walking in a random direction for a random number of steps.<br />
  ![img](/screenshots/004_learn_turtle.jpg)
- **spiro_turtle.py**: This program draws a rainbow spirograph image using Turtle.<br />
  ![img](/screenshots/004_rainbow_spiro_b.jpg)
- **spiral_spiro.py**: This program draws a green spiral spirograph image using Turtle.<br />
  ![img](/screenshots/004_spiral_spiro.jpg)

**Thoughts:** Feeling a little frustrated that this repo will not have the commit history of the first 3 days, but I hope things go more smoothly from here. I'm excited to learn turtle and graphics libraries, instead of creating purely terminal-based programs.

-----

## Day 3. Python Functions, Dictionaries, and Nesting Lists
### January 14, 2023

**Today's Progress**: 
- Continued working through "100 Days of Python" Udemy class. Completed days 8-11.
- Focused on function parameters (positional and keyword), dictionaries, nesting lists and dictionaries, docstrings, and dipping a little into classes/OOP.

**Programs**:
- **primenumber.py**: Checks whether or not a given number is a prime number.<br />
  ![img](/screenshots/003_prime_1.jpg)   ![img](/screenshots/003_prime_2.jpg)
- **caesarcipher.py**: Uses the Caesar Cipher mode of encryption to encode or decode secret messages.<br />
  ![img](/screenshots/003_caesar.jpg)
- **calculator.py**: Acts as a calculator that can perform basic math operations for the user.<br />
  ![img](/screenshots/003_calc.jpg)
- **blackjack.py**: A standard game of blackjack. Creates a shuffled deck of 52 cards, keeps track of the player and dealer's hands, calculates hand values, handles the dealer's decisions, and determines the winner/outcome. It also figures out when to count an ace as 1 or 11.<br />
  ![img](/screenshots/003_blackjack_b.jpg)

**Thoughts:** I continued working on exercises from the "100 Days of Python" class and adding a little more complexity to them. The Blackjack project was supposed to be a lot simpler (just pulling random values from a list of possible card values, with no classes). However, I felt confident to try including classes and more complicated game logic (creating a full deck of 52 cards, using logic to determine when aces should be counted as 1 vs 11, and creating classes with initializers for the Cards, Deck, and Hands). Having fun pushing myself :)

-----

## Day 2. Randomization, Loops, and Validating Input
### January 13, 2023

**Today's Progress**: 
- Continued working through "100 Days of Python" Udemy class. Completed days 4-7.
- Focused on validating input, randomization, loops, and functions.

**Programs**:
- **numberguesser.py**: A game that asks the player to guess a secret random number between 1 and 1000 within 10 guesses. Incorporates a basic game loop and input validation.<br />
    ![img](/screenshots/002_number_guesser.jpg)
- **rockpaperscissors.py**: A simple Rock, Paper, Scissors game. The player enters their choice while the computer picks a random choice. Then the program shows ASCII art of each choice and determines the winner.<br />
    ![img](/screenshots/002_rps.jpg)
- **fizzbuzz.py**: A classic interview challenge. Print out each integer from 1 to 100, unless it's divisible by 3, 5, or 15. In those cases, write special keywords instead.<br />
    ![img](/screenshots/002_fizzbuzz.jpg)
- **passwordgen.py**: Generates a random, secure password with a given number of letters, symbols, and numbers.<br />
    ![img](/screenshots/002_password_gen.jpg)
- **hangman.py**: A classic game in which the computer chooses a random word, and the player guesses which letters are in it. If they guess all the letters in the word without too many mistakes, they win. If they make too many wrong guesses, they hang.<br />
    ![img](/screenshots/002_hangman_1.jpg) ![img](/screenshots/002_hangman_2.jpg)

**Thoughts:** Feeling pretty comfortable with playing around with lists, loops, and basic functions.

-----

## Day 1. Hello World
### January 12, 2023

**Today's Progress**: 
- Started with a Hello World program, of course.  
- Set up VSCode and Github for this 100-day project.
- Began refreshing knowledge of Python fundamentals by looking at tutorials and playing around with the editor.
- Signed up for "100 Days of Python" Udemy class for learning and inspiration. Completed days 1-3.

**Programs**:
- **helloworld.py**: Basic "hello world" program, with some ASCII art.<br />
    ![helloworld](/screenshots/001_hello_world.jpg)
- **basicmath.py**: Asks the user for two numbers, then performs simple math operations with those numbers.<br />
    ![img](/screenshots/001_basic_math.jpg)
- **weightconversion.py**: Asks the user for their weight in pounds, then converts it to kg, stones, and a variety of silly measurements.<br />
    ![img](/screenshots/001_weight.jpg)
- **tipcalculator.py**: Asks the user for a bill total and how many people will split the bill. Calculates and displays a table with common tip amounts and how much each person should pay.<br />
    ![img](/screenshots/001_tip.jpg)

**Thoughts:** It's been a while since I've used Python, and Python 3 syntax has changed in a few ways since Python 2, so I decided to start from the beginning with some very simple projects. I feel excited and determined.

