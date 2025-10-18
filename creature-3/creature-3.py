import py5

class Tiny:
    # Set the Tiny's start position, velocity, and size
    def __init__(self, x, y, size = 20):
        self.size = size
        self.pos = py5.Py5Vector(x, y)
        self.vel = py5.Py5Vector(py5.random(-2, 2), py5.random(-2, 2))

    def move(self):
        # define hitbox size
        hitbox = self.size

        # tiny moves in random direction upon spawn
        self.pos += self.vel

        # if the mouse hovers over the tiny, the direction of movement changes
        if (py5.mouse_x > self.pos.x - hitbox and py5.mouse_x < self.pos.x + hitbox):
            if (py5.mouse_y >= self.pos.y - hitbox and py5.mouse_y < self.pos.y + hitbox):
                self.vel = py5.Py5Vector(py5.random(-2, 2), py5.random(-2, 2))
                
    
    # This is what will be drawn/displayed
    def display(self):
        py5.push_matrix()
        py5.translate(self.pos.x, self.pos.y)
        py5.fill(255)
        py5.no_stroke()

        # tiny monster!
        py5.ellipse(0, 0, self.size, self.size)
        py5.arc(0, -self.size, self.size, self.size, 0, py5.PI)

        # arms
        arm_offset_x = self.size * 0.75
        arm_size = self.size * 0.5
        py5.ellipse(-arm_offset_x, 0, arm_size, arm_size)
        py5.ellipse(arm_offset_x, 0, arm_size, arm_size)

        # legs
        feature_offset_x = self.size * 0.2
        leg_offset_y = self.size * 0.75
        leg_size = self.size * 0.4
        py5.ellipse(-feature_offset_x, leg_offset_y, leg_size, leg_size)
        py5.ellipse(feature_offset_x, leg_offset_y, leg_size, leg_size)

        py5.pop_matrix()

tinies = []

# Setup
def setup():
    # Canvas size and padding
    py5.size(800, 800)
    # Background color
    py5.background(0)

def draw():
    py5.background(0)
    # spawn the tiny and it will move
    for tiny in tinies:
        tiny.move()
        tiny.display()

def mouse_pressed():
    # Create a new Tiny object at the current mouse position
    new_tiny = Tiny(py5.mouse_x, py5.mouse_y)

    # Add tiny to array
    tinies.append(new_tiny)

py5.run_sketch()