#!/usr/bin/python3
"""
    class Square implements class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square implements rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square object."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width ,ust be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square."""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        """Assigns attributes using *args and **kwargs."""
        if args:
            arg_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(arg_names):
                    setattr(self, arg_names[i], arg)
                else:
                    break
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
