#!/usr/bin/python3
"""
Defines rectangle class which inherits from base
"""
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle implements Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            initializes the instance of the class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            getter method for __width
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter method for __width
            Args:
                value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            getter method for height
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter method for height
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            getter method for x.
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter method for x.
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            getter method for y
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter method for y
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            calculates and returns the area of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
            Displays the rectangle using '#' characters
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
            Returns string reepresentation of the rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
