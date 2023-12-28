class MarsRover:
    DIRECTIONS = {'N': (0, -1), 'S': (0, 1), 'E': (-1, 0), 'W': (1, 0)}
    LEFT_ROTATION = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    RIGHT_ROTATION = {v: k for k, v in LEFT_ROTATION.items()}

    def __init__(self, location, direction, grid_size):
        if direction not in self.DIRECTIONS:
            raise ValueError(f"Invalid direction: {direction}")
        self.x, self.y = location
        self.direction = direction
        self.grid_width, self.grid_height = grid_size

    def move_forward(self):
        dx, dy = self.DIRECTIONS[self.direction]
        self.x = (self.x + dx) % self.grid_width
        self.y = (self.y + dy) % self.grid_height

    def move_backward(self):
        dx, dy = self.DIRECTIONS[self.direction]
        self.x = (self.x - dx) % self.grid_width
        self.y = (self.y - dy) % self.grid_height

    def turn_left(self):
        self.direction = self.LEFT_ROTATION[self.direction]

    def turn_right(self):
        self.direction = self.RIGHT_ROTATION[self.direction]

    def execute_commands(self, commands):
        for command in commands:
            print("***** " + self.direction+  " " + str(self.x) + ", " + str(self.y))

            if command == 'f':
                self.move_forward()
            elif command == 'b':
                self.move_backward()
            elif command == 'l':
                self.turn_left()
            elif command == 'r':
                self.turn_right()
        

    def current_location(self):
        return (self.x, self.y)

    def current_direction(self):
        return self.direction
