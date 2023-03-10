# Snake class for the snake game project.
from turtle import Turtle, Screen

# Directions for Turtle setheading()
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    """Class to handle the snake object in the game, including creating 
    its body segments, handling its movement, and changing its direction."""
    def __init__(self):
        # The height/width of each square segment of the snake's body
        self.SEGMENT_SIZE = 20

        # The number of pixels to move at a time.
        self.STEP_DISTANCE = 20

        # A list to hold each turtle segment of the snake's body
        self.segments = []
        self.create_body()
        self.head = self.segments[0]

    def create_body(self):
        """Create the 3 starting body segments of the snake."""

        for i in range(3):
            position = ((i * -self.SEGMENT_SIZE), 0)
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment to the snake.
        Arg position (tuple): a tuple of 2 integers for the x and y position"""
        t = Turtle(shape="square")
        t.color("white")
        t.width(self.SEGMENT_SIZE)
        t.penup()
        t.goto(position)

        self.segments.append(t)

    def extend(self):
        """Add a new segment to the snake, at the position of the current
        tail of the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward in its current direction."""

        # Starting with the tail tip, move each segment of the
        # body to where the segment in front of it is.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        # Move the first segment forward.
        self.head.forward(self.STEP_DISTANCE)

    def go_up(self):
        """Set the snake direction to go upward 
        (if it's not currently facing downward)."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        """Set the snake direction to go downward 
        (if it's not currently facing upward)."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        """Set the snake direction to go left 
        (if it's not currently facing right)."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        """Set the snake direction to go right 
        (if it's not currently facing left)."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
