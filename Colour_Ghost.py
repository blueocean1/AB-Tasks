from random import choice


class Ghost(object):
    def __init__(self):
        self.colours = ["white", "yellow", "purple", "red"]
        self.colour = choice(self.colours)
