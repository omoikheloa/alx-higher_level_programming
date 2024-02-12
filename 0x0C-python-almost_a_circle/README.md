**Almost a Circle - Python Project**

This project aims to create a comprehensive set of classes and functionalities to handle geometric shapes, specifically rectangles and squares, in Python. The classes are designed to manage attributes such as dimensions, position, and identification for these shapes.

**Table of Contents**
*Introduction
*Project Structure
*Class Hierarchy
*Functionality
*How to Use
*Contributing
*License

*Introduction*
The project involves creating classes for rectangles and squares, along with a base class to handle common functionalities such as identification and serialization/deserialization. The classes are designed to be flexible and extensible, allowing for easy addition of new shapes or features in the future.

*Project Structure*
The project directory structure is as follows:


	models/
	│
	├── __init__.py
	├── base.py
	├── rectangle.py
	└── square.py

__init__.py: Empty file to make models a Python package.
base.py: Contains the Base class with common functionalities.
rectangle.py: Defines the Rectangle class, inheriting from Base.
square.py: Defines the Square class, inheriting from Rectangle.

*Class Hierarchy*
Base: Manages common attributes and methods for all shapes.
Rectangle: Represents a rectangle with width, height, and position.
Square: Represents a square, a special case of a rectangle.

*Functionality*
The project implements the following functionalities:

Creation of rectangles and squares with specified dimensions and positions.
Calculation of area for rectangles and squares.
Displaying shapes on the console.
Serialization and deserialization of shape objects to/from JSON and CSV formats.
Loading and saving shapes to files.

*How to Use*
To use the classes and functionalities provided by this project:

Clone the repository to your local machine.
Import the necessary classes from the models package in your Python scripts.
Create instances of Rectangle or Square objects and use their methods to perform various operations.
Example usage:

	python
	from models.rectangle import Rectangle
	from models.square import Square

	# Create a rectangle with width 10, height 5, and position (x=2, y=3)
	rect = Rectangle(width=10, height=5, x=2, y=3)

	# Calculate and print the area of the rectangle
	print("Area:", rect.area())

	# Create a square with size 7 and position (x=0, y=0)
	square = Square(size=7, x=0, y=0)

	# Display the square
	square.display()

*Contributing*
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or pull request on GitHub.

*License*
This project is licensed under the MIT License.
