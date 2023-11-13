#!/usr/bin/python3
"""define the Base model class"""


class Base:
    """Base class model.

    representation of the "base" for all other classes in this project.

    private class Attributes:
        __nb_object (int): number of Base instances.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of a new Base.

        Args:
            id (int): Base class id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
