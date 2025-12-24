# Challenge Overview
Build an interactive program that helps users calculate the area of different shapes.

* Start with: "I can calculate the area of a shape for you. Which shape do you want me to calculate the area of?"
* Accept shape names such as circle, rectangle, square, or triangle (case insensitive is a plus).
* Prompt for the correct measurements based on the chosen shape and apply the proper area formula.
* Handle invalid inputs gracefully (unexpected shapes or non-numeric measurements).
* Follow the UCASE strategy and limit focused time to about one hour.

# U | Understand
A function that returns the area of a shape given the provided measurments.

# C | Clue Detection
* Input: String (use input()), Float (use input()) 
* Output: Float (use return statement)
* Clues:
    * "proper area formula": breakdown the program into the caculator and area formula functions
    * "choosen shape": if statements do obtain corresponding measurments and area formula
    * "unexpected shapes and non-numeric measurments": while loop to coutinue iteration until the users input is valid. 
    * "case insesitive is a plus": use lower().

# A | Assemble
1) Function Decleration: def calculator()
2) Print brief message to introduce user on what the program does.
3) Create a variable with a list of lowercased shape names that the calculator can find the area for.
4) Enter while loop. Ask for the name of the shape and use lower() to lowercase the input. Compare the user's shape to the list of
   available shapes, notify the user if shape entered is not available and begin a new loop iteration.
5) Use if statements to then ask for further measurments and plug them into the area formula.
6) Define an area formula for each shape.

# S | Solve
see Calculator.py

I created a function that starts by introducing the user and asking for the shape they are looking to find the area for. Then I used a while loop and try/except to collect the proper measurements for the shape they selected. These measurements are then passed into functions that contain the appropriate area formula. The answer then prints as a float.

# E | Examine
